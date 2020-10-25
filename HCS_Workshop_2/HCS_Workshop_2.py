import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.blogto.com/restaurants/")

soup = BeautifulSoup(page.content,'html.parser')
items = soup.find_all('div', attrs={'class':'listing-thumbnail-grid-item blogto-grid-item'})

for item in items:
    print(item.p.get_text().strip())
