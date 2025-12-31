from rest_framework.test import APIClient
from django.urls import reverse
import json

client = APIClient()

def print_res(label, response):
    print(f"\n--- {label} ---")
    print(f"Status: {response.status_code}")
    print(f"Data: {json.dumps(response.data, indent=2)}")

# Create
r_create = client.post(reverse('create-task'), {'title': 'Shell Test', 'description': 'Testing via shell'}, format='json')
print_res('Testing Create', r_create)
if r_create.status_code != 201:
    exit()

tid = r_create.data['data']['id']

# List
r_list = client.get(reverse('list-tasks'))
print_res('Testing List', r_list)

# Get
r_get = client.get(f"{reverse('get-task')}?task_id={tid}")
print_res('Testing Get', r_get)

# Update
r_update = client.put(f"{reverse('update-task')}?task_id={tid}", {'title': 'Updated', 'description': 'Updated desc', 'is_completed': True, 'task_id': tid}, format='json')
print_res('Testing Update', r_update)

# Delete
r_delete = client.delete(f"{reverse('delete-task')}?task_id={tid}")
print_res('Testing Delete', r_delete)
