
from bs4 import BeautifulSoup
import requests

baidu = requests.get("https://www.baidu.com").content

soup = BeautifulSoup(baidu,"html.parser")

# print(soup.text)

links = soup.findAll('a')  #  <a> 标签在 html中 是超链接的 标签，其中的内容是李恩杰

for link in links:  #遍历所有 link
    print(link.string)  #只显示 link元素中的 字符串元素
