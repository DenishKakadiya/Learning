import webbrowser
import requests
from bs4 import BeautifulSoup


url = "https://www.google.com"

response = requests.get(url)
print(response)
