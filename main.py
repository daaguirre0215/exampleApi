import requests

URL = 'https://httpbin.org/cookies'

cookies = {
    'dni':'2903',
    'user':'daguirre',
    'age':'22',
    'potition':'devjr',
}

response = requests.get(URL, cookies=cookies)

if response.status_code ==200:
    print(response.json())

