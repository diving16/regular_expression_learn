import requests
from bs4 import BeautifulSoup

response=requests.get('https://www.douban.com/group/blabla/')

#不允许爬的
#https://www.douban.com/robots.txt

a=response.text

soup=BeautifulSoup(a,'html.parser')

print(soup.title)
print(soup.p)