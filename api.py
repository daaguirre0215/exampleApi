import requests
#Permite poder descargar cualquier tipo de archivo

URL = 'https://scontent.fsal3-1.fna.fbcdn.net/v/t39.30808-6/340499731_2384608105041480_1886526679553193352_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=_0MLXTwm2tQAX_S00MD&_nc_ht=scontent.fsal3-1.fna&oh=00_AfDK41Y5bwaobbKxLzI0fW6HB8-TTnBYZNj1N5XWdVSjzA&oe=647E3DFC' #Imagen PNG

response = requests.get(URL, stream=True)

if response.status_code == 200:
    with open('images/yo.png', 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
