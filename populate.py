import requests

data = {
    'name': 'Object 1',
    'description': 'Description of object 1',
}
response = requests.post('http://localhost:8000/mymodels/', json=data)
print(response.status_code)
print(response.json())