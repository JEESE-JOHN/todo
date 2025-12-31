from rest_framework.test import APIClient
from django.urls import reverse
import json

client = APIClient()

def print_res(label, response):
    print(f"\n--- {label} ---")
    print(f"Status: {response.status_code}")
    print(f"Data: {json.dumps(response.data, indent=2)}")

# Create
r_create = client.post(reverse('music-create'), {'title': 'Song 1', 'artist': 'Artist 1'}, format='json')
print_res('Testing Music Create', r_create)
if r_create.status_code != 201:
    exit()

sid = r_create.data['data']['id']

# List
r_list = client.get(reverse('music-list'))
print_res('Testing Music List', r_list)

# Get
r_get = client.get(f"{reverse('music-get')}?song_id={sid}")
print_res('Testing Music Get', r_get)

# Update
r_update = client.put(f"{reverse('music-update')}?song_id={sid}", {'title': 'Song Updated', 'artist': 'Artist Updated'}, format='json')
print_res('Testing Music Update', r_update)

# Delete
r_delete = client.delete(f"{reverse('music-delete')}?song_id={sid}")
print_res('Testing Music Delete', r_delete)
