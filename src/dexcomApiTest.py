import requests
import http.client
import json
from bs4 import BeautifulSoup

client_id = 'Rh4AFVzVJftcHQlDr0x9uRIETUeaLd6v'
client_secret = 'gpUhIdCmdsPN6CnI'

redirect_uri = 'http://localhost:8000'

loginLink = 'https://api.dexcom.com/v2/oauth2/login?client_id=' \
            + client_id + '&redirect_uri=' \
            + redirect_uri + '&response_type=code&scope=offline_access'

print(loginLink)

auth_code = input("Enter the auth code: ")

conn = http.client.HTTPSConnection("api.dexcom.com")

payload = 'client_secret=' \
          + client_secret + '&client_id=' \
          + client_id + '&code=' \
          + auth_code + '&grant_type=authorization_code&redirect_uri=' \
          + redirect_uri

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

conn.request("POST", "/v2/oauth2/token", payload, headers)

res = conn.getresponse()
data = res.read()
data_json = json.loads(data.decode("utf-8"))

access_token = data_json['access_token']

print(access_token)

# Making a request

headers = {
    'authorization': 'Bearer ' + access_token
    }

start_date = '2022-02-06T15:30:00'
end_date = '2022-02-06T15:45:00'

conn.request("GET", '/v2/users/self/egvs?startDate=' + start_date + '&endDate=' + end_date, headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))







