import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'oTAGsADKf7ZeHv3L06L34cfkBzhNYqwknhNWj8Zg'}
response = requests.get(url, params)

if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])
    for key, value in enumerate(photos):
        img_url = value.get('img_src')
        if img_url:
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                file_name = f'photo_{key+1.}.jpg'
                with open(file_name, 'wb') as file:
                    file.write(img_response.content)

