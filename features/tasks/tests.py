from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from features.tasks.models import Task

class TaskAPITests(APITestCase):
    def test_task_lifecycle(self):
        # 1. Create
        create_url = reverse('create-task')
        data = {'title': 'Test Task', 'description': 'Testing description'}
        response = self.client.post(create_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['status'])
        self.assertEqual(response.data['data']['title'], 'Test Task')
        task_id = response.data['data']['id']

        # 2. List
        list_url = reverse('list-tasks')
        response = self.client.get(list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['status'])
        self.assertGreaterEqual(len(response.data['data']['data']), 1)

        # 3. Get
        get_url = f"{reverse('get-task')}?task_id={task_id}"
        response = self.client.get(get_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['id'], task_id)

        # 4. Update
        update_url = f"{reverse('update-task')}?task_id={task_id}"
        update_data = {
            'title': 'Updated Title',
            'description': 'Updated description',
            'is_completed': True,
            'task_id': task_id
        }
        response = self.client.put(update_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['title'], 'Updated Title')
        self.assertTrue(response.data['data']['is_completed'])

        # 5. Delete
        delete_url = f"{reverse('delete-task')}?task_id={task_id}"
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Task.objects.filter(id=task_id).exists())
