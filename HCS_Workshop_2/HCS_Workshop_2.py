import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.blogto.com/restaurants/")

soup = BeautifulSoup(page.content,'html.parser')
items = soup.find('div',attrs={'listing-criteria-list-wrapper'}).find_all('a', attrs={'class':'listing-criteria-link'})

for item in items:
    print(item.get_text().strip())
    link = requests.get("https://www.blogto.com/restaurants/c/toronto/" + item.get_text().strip().lower() + '/')
    smallSoup = BeautifulSoup(link.content, 'html.parser')
    restaurants = smallSoup.find('div', attrs={'class':'listings-navigator-content'}).find('script',attrs={'type':'text/javascript'})
    print(restaurants)
    #for restaurant in restaurants:
     #   print('check')
      #  print(restaurant.get_text())
