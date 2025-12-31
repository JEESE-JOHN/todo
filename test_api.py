import os
import django
import sys
from rest_framework.test import APIClient
from django.urls import reverse

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_project.settings')
django.setup()

def test_api():
    client = APIClient()
    
    print("--- Testing Create Task ---")
    create_url = reverse('create-task')
    data = {"title": "Test Task", "description": "This is a test task"}
    response = client.post(create_url, data, format='json')
    print(f"Status: {response.status_code}")
    print(f"Response: {response.data}")
    
    if response.status_code != 201:
        print("Create Task Failed")
        return
        
    task_id = response.data['data']['id']
    
    print("\n--- Testing List Tasks ---")
    list_url = reverse('list-tasks')
    response = client.get(list_url)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.data}")
    
    print("\n--- Testing Get Task ---")
    get_url = f"{reverse('get-task')}?task_id={task_id}"
    response = client.get(get_url)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.data}")
    
    print("\n--- Testing Update Task ---")
    update_url = f"{reverse('update-task')}?task_id={task_id}"
    # Note: The serializer expects task_id in the body as well based on my view of update.py
    update_data = {"title": "Updated Task", "description": "Updated description", "is_completed": True, "task_id": task_id}
    response = client.put(update_url, update_data, format='json')
    print(f"Status: {response.status_code}")
    print(f"Response: {response.data}")
    
    print("\n--- Testing Delete Task ---")
    delete_url = f"{reverse('delete-task')}?task_id={task_id}"
    response = client.delete(delete_url)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.data}")

if __name__ == "__main__":
    test_api()
