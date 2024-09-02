from app.app import upload_image, get_image, delete_image
import requests
from urllib.parse import quote

url = 'http://127.0.0.1:8080'
url_get= '/image/'

# Post
with open('photo_1.0.jpg', 'rb') as image_file:
    files = {'image': image_file}
    response = requests.post(f'{url}/upload', files=files)
    if response.status_code == 201:
        print('Изображение загружено')
        print('URL изображения:', response.json().get('image_url'))
    else:
        print('Ошибка при загрузке:', response.json())


#Get
filename = 'photo_1.0.jpg'
encoded_filename = quote(filename)
headers = {'Content-Type': 'text'}

response = requests.get(f'{url}/image/{encoded_filename}', headers=headers)
if response.status_code == 200:
    image_url = response.json().get('image_url')
    print('Get URL:', image_url)
else:
    print('Ошибка при получении URL:', response.json())


#Delete
response = requests.delete(f'{url}/delete/{encoded_filename}')
if response.status_code == 200:
    print('Изображение успешно удалено:', response.json().get('message'))
else:
    print('Ошибка при удалении изображения:', response.json())