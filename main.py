import requests
from datetime import datetime
import os

USERNAME = os.getenv('USER')
TOKEN = os.getenv('TOKEN')
ID = 'graph01'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsofService': 'yes',
    'notMinor': 'yes'
}

# CREATE ACC
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_params = {
    'id': ID,
    'name': 'Programming Graph',
    'unit': 'Hours',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# CREATE GRAPH
#response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#print(response.text)

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{ID}'

today = datetime.now()
t = today.strftime("%Y%m%d")
print(t)

pixel_params = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '2.5'
}

# ADD PIXEL
#response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
#print(response.text)

update_pixel_endpoint = f'{pixel_endpoint}/{USERNAME}/graphs/{ID}/{t}'

update_params = {
    'quantity': '2.2'
}

# UPDATE GRAPH
response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
print(response.text)