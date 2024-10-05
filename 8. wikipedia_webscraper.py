import requests
from bs4 import BeautifulSoup

#get wikipedia main page
response = requests.get("https://en.wikipedia.org/wiki/Main_Page").text
soup = BeautifulSoup(response,'lxml')

#get "on this day" div and print title
div = soup.find(id="mp-otd")
day = div.p.a.text
print(f"On this day ({day}), these events occured in past:")

#get "On this day" event list and print it.
for index, list in enumerate(div.ul.find_all('li')):
    print(f'{index +1}: {list.text}')


# print(soup.prettify())