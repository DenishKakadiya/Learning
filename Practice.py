import requests
import bs4


payload = {
    "username": 'Dk',
    "password": 'testing'
}
response = requests.get('https://httpbin.org/delay/2', timeout=3)
print(response)


""" with open("../Practice/comic.png","wb") as f:
    f.write(response.content) """