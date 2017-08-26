# Client that interfaces with server for testing API endpoints.

import requests
import json
from pymongo import MongoClient
import time
headers = {'Content-Type': 'application/json'}
api_endpoint='http://localhost:5000/api/v1.0'

def api_post(endpoint,payload=None):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post('{}{}'.format(api_endpoint, endpoint), data=json.dumps(payload),headers=headers)
    return response

def api_get(endpoint, params=None):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get('{}{}'.format(api_endpoint, endpoint), params=params,headers=headers)
    return response


def test_register(payload):
    response = api_post('/register', payload)
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return None


def main():
    user_payload = {
        "user":"andy",
        "pass":"password",
        "email":"andy@yahoo.com",
        "user_fullname":"Andy Lien",
    }
    test_register(user_payload)


if __name__ == '__main__':
    main()