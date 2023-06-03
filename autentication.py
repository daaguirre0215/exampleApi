import requests
from getpass import getpass

URL = 'https://httpbin.org/basic-auth/ola/123' 

password = getpass('Ingresa la contraseña: ')

session = requests.Session()
session.auth = ('ola',password)



response = session.get(URL)

if response.status_code == 200:
    print('Conexión establecida...',response.json())


if response.status_code == 401:
    print('Error en contraseña')



