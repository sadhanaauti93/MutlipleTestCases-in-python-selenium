import requests
import json
import jsonpath

def test_Add_new_data():
    # Adding as print
    Add_URL="http://thetestingworldapi.com/api/studentsDetails"
    f = open('F:\\PostFile.Json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(Add_URL,request_json)
    print(response.text)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    # Technical Details
    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    f = open('F:\\TechDetails.Json', 'r')
    request_json = json.loads(f.read())
    request_json['id']=int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(tech_api_url, request_json)
    print(response.text)

    #Address Detials
    add_api_url = "http://thetestingworldapi.com/api/addresses"
    f = open('F:\\Address.Json', 'r')
    request_json = json.loads(f.read())
    request_json['stid'] = id[0]
    response = requests.post(add_api_url, request_json)
    print(response.text)

    #Fetching the complet deatil
    final_Details="http://thetestingworldapi.com/api/studentsDetails/+str(id[0])"
    response = requests.get(final_Details)
    print(response.text)

