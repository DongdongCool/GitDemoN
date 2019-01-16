
from bs4 import BeautifulSoup
import requests

data = requests.get("https://www.baidu.com").content

soup = BeautifulSoup(data,"html.parser")

# print(soup.text)
#
# links = soup.findAll('a')  #  <a> 标签在 html中 是超链接的 标签，其中的内容是李恩杰
#
# for link in links:  #遍历所有 link
#     print(link.string)  #只显示 link元素中的 字符串元素

print(soup.title.text)  # 获取网页上的 各种元素 使用 不同的标签来搜索

# print(soup.)
