import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import time

driver = webdriver.Chrome()

page = requests.get("https://www.blogto.com/restaurants/")

soup = BeautifulSoup(page.content,'html.parser')
items = soup.find('div',attrs={'listing-criteria-list-wrapper'}).find_all('a', attrs={'class':'listing-criteria-link'})

with open('restaurants.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Restaurant', 'Category', 'Neighborhood', 'Address', 'Phone Number', 'Rating'])
    for item in items:
        print(item.get_text().strip()) 
        driver.get("https://www.blogto.com/restaurants/c/toronto/" + item.get_text().strip().lower() + '/')
        html = driver.page_source

        smallSoup = BeautifulSoup(html, 'html.parser')
        restaurants = smallSoup.find_all('li', attrs={'class':'listing-search-result-item'})

        for restaurant in restaurants:
            tag = restaurant.find('a', attrs={'class':'listing-search-result-picture-link'})
            link = tag.get('href')
            moreinfo = driver.get(link)
            html2 = driver.page_source
            smallestSoup = BeautifulSoup(html2, 'html.parser')
            time.sleep(0.1)
            li = [item.get_text().strip()]
            li.append(restaurant.find('p', attrs={'class':'listing-search-result-name'}).get_text())     
            li.append(restaurant.find('span', attrs={'class':'listing-search-result-category-info-item'}).get_text())
             
            if smallestSoup.find('a', attrs={'href':'#address'}):
                li.append(smallestSoup.find('a', attrs={'href':'#address'}).get_text())
            else:
                li.append('Not Found')

            if smallestSoup.find('a', attrs={'class':'listing-badge-phone-link'}):
                li.append(smallestSoup.find('a', attrs={'class':'listing-badge-phone-link'}).get_text())
            else:
                li.append('Not Found')
           
            li.append(restaurant.find('div', attrs={'class':'rating-star-medium-text'}).get_text())
            writer.writerow(li)
