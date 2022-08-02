from email import header
from bs4 import BeautifulSoup
import requests
from csv import writer 

url_obj = "https://www.startech.com.bd/laptop-notebook/laptop"
page = requests.get(url_obj)

#print (page)

soup = BeautifulSoup(page.content, 'html.parser')

#print (soup)

lists = soup.find_all('div', class_="p-item")
print (len(lists))

# title = lists.find_all('a', class_="listing-search-item__link--title")
# print (title)
# with open('info.csv', 'w', encoding='utf8', newline='') as f:
#     callwriter = writer(f)
#     header = ['title', 'price','location', 'area']
#     callwriter.writerow(header)

        
#     for list in lists:
#         title = list.find('a', class_="listing-search-item__link--title").text.replace('\n', '')
#         location = list.find('div', class_="listing-search-item__location").text.replace('\n', '')
#         price = list.find('div', class_="listing-search-item__price").text.replace('\n', '')
#         area = list.find('li', class_="illustrated-features__item--surface-area").text.replace('\n', '')
#         all_info = [title, price, location, area]
#         # print(info)
#         callwriter.writerow(all_info)

