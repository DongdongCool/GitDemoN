
from bs4 import BeautifulSoup
import requests

baidu = requests.get("http://daz.lianghuadashi.com/category/daz/").content

soup = BeautifulSoup(baidu,"html.parser")

# print(soup.text)

links = soup.findAll('img')  #  <a> 标签在 html中 是超链接的 标签，其中的内容是李恩杰

for link in links:  #遍历所有 link
    print(link)  #只显示 link元素中的 字符串元素
