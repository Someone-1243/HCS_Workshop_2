import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re

driver = webdriver.Chrome()

page = requests.get("https://www.blogto.com/restaurants/")

soup = BeautifulSoup(page.content,'html.parser')
items = soup.find('div',attrs={'listing-criteria-list-wrapper'}).find_all('a', attrs={'class':'listing-criteria-link'})

for item in items:
    print(item.get_text().strip()) 
    driver.get("https://www.blogto.com/restaurants/c/toronto/" + item.get_text().strip().lower() + '/')
    html = driver.page_source
    smallSoup = BeautifulSoup(html, 'html.parser')
    restaurants = smallSoup.find_all('a', attrs={'class':'listing-info-box-name-link'})
    for restaurant in restaurants:
        print(restaurant.get_text())
    print('--------')
    print()
