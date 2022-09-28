import requests

r = requests.get('http://127.0.0.1:5000/id/Claude')
print(r.text)

r = requests.post('http://127.0.0.1:5000/new', headers={"Content-Type":"application/json"}, json = '{"id": "3", "name": "uncle egg", "age": 234}')
print(r.text)

r = requests.get('http://127.0.0.1:5000/id/uncle egg')
print(r.text)

r = requests.get('http://127.0.0.1:5000/users')
print(r.text)