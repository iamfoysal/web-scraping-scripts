import csv
from unittest import result
from bs4 import BeautifulSoup
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions

# driver = webdriver.Chrome()

options =EdgeOptions()
options.use_chromium = True
driver=  Edge (options= options)

url= 'https://www.amazon.com'
driver.get(url)
# print(driver)

def getUrl(search_term):
    template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1'
    search_term = search_term.replace(' ', '+')
    return template.format(search_term)

url = getUrl('ultrawide monitor')
# print(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
# print (soup)

data =soup.find_all('div', {'data-component-type':'s-search-result'})

# print(data)
def main_data(item):
    item = data[0]
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.com'+ atag.get('href')

    pricess = item.find('span', 'a-price')
    price = pricess.find('span', 'a-offscren').text
    rating = item.i.text
    # print(rating)
    review= item.find ('span', {'class': 'a-size-base', 'div': 'auto'}).text

    all_result = (description,price,rating,review, url)
    print (all_result)


