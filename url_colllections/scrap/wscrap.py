from urllib.request import urlopen
from bs4 import BeautifulSoup


url_az = "https://www.bbc.com"
filepath = "html/bbc.html"

class AmazonScraper:
	__url = ''
	__data = ''
	__wlog = 'None'
	__soup ='None'

	def __init__(self, url, wlog):

		self.__url=url
		self.__wlog = wlog


	def retrive_webpage(self):
		try:
			html = urlopen(self.__url)

		except Exception as e:

			print(e)
			self.__wlog.result(e)
		else:
			self.__data = html.read()
			if len (self.__data)> 0:
				print("retriver Success")


	def write_web_page(self, filepath=filepath, data ='' ):
		try:
			with open(filepath,'wb')as obj:
				if data:
					obj.write(data)
				else:
					obj.write(self.__data)
		except Exception as e:
			print (e)

	def read_web_page(self, filepath=filepath):
		try:
			with open(filepath)as obj:
				self.__data= obj.read()

		except Exception as e:
			#print (e)
			self.__wlog.result(str(e))

	def change_url(self, url):
		self.__url= url

	def print_data(self):
		print(self.__data)


	def convate_to_soup(self):
		self.__soup =BeautifulSoup(self.__data, "html.parser")

	def parseSope_to_html(self):
		
		list= self.__soup.find_all(['h1','h2','h3','h4', 'h5' ])
		# print(list)
		# for link in soup.find_all('a'):
        #     link_name  = link.string
        #     link_address = link.get('href')

		html_txt= '''
		<html lang="en">
		<head>
			<title>Scraping</title>
		</head>
		<body>
			{NEWS_LINK}
		</body>
		</html>
		'''

		news_link= '<ol>'

		for tag in list:
			
			if tag.parent.get('href'):
				link = self.__url + tag.parent.get('href')
				# domain = 'https://www.bbc.com'
				#link = tag.parent.get('href')
				title = tag.string
				news_link+= "<li><a href={} target='_blank'>{}</li>\n".format(link,title)
		news_link +='</ol>'

		html_txt = html_txt.format(NEWS_LINK=news_link)
		self.write_web_page(filepath = 'html/newssource.html', data= html_txt.encode())

