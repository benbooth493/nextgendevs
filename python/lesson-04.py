import requests


def get_user(name):
    r = requests.get("http://127.0.0.1:5000/id/{}".format(name))
    return r.text


def create_user(payload):
    r = requests.post(
        "http://127.0.0.1:5000/new",
        headers={"Content-Type": "application/json"},
        json=payload,
    )
    return r.text


def get_all_users():
    r = requests.get("http://127.0.0.1:5000/users")
    return r.text


print(get_user("Ben"))

data_payload = '{"id": "3", "name": "uncle egg", "age": 234}'
print(create_user(data_payload))

print(get_all_users())
