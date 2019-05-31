# from django.test import TestCase
import json, requests


BASE_URL = 'http://127.0.0.1:8000'
ENDPOINT = '/task/'
url = BASE_URL + ENDPOINT


# Create your tests here.
def create_resource():
    data = {
        'title': 'My Birthday is gone :(',
        'date_to_do': '2018-07-01'
    }
    resp = requests.post(url, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())


def update_resource(id):
    data = {
        'check': 'True'
    }
    resp = requests.put(url+str(id)+'/', data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())


def delete_resource(id):
    resp = requests.delete(url+str(id)+'/')
    print(resp.status_code)
    print(resp.json())


# create_resource()
# update_resource(7)
delete_resource(15)  # change id to existing database resource
