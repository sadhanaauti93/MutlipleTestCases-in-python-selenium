import requests
import json
import jsonpath

#API URL
url = "https://reqres.in/api/users"


def test_create_new_user():
    # Read Input Json File
    file = open('F:\\CreatUser.Json','r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url,request_json)
    assert response.status_code == 201



def test_create_other_user():
    # Read Input Json File
    file = open('F:\\CreatUser.Json','r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url,request_json)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json,'id')
    print(id[0])