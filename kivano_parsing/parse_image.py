import requests

image_url = 'https://static.wikia.nocookie.net/siivagunner/images/4/40/Gachimuchi.jpg/revision/latest?cb=20181204024544'

response = requests.get(image_url)

with open('image.jpg', 'wb') as f:
    f.write(response.content)