
from bs4 import BeautifulSoup

myHtml = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>this is my title</title>
</head>
<body>
<h1>This is H1,love you </h1>
<h1>这是另外一个 H1 </h1>
<h2>This is H2,小一点的字体 </h2>
<p>this is inty, i love you gays. yes!!!  </p>
</body>
</html>

'''
# 读取字符串 ， 特征是 html的解析器
soup1 = BeautifulSoup(myHtml,'html.parser')

myH1 = soup1.findAll("h1")  #解析器中查找 h1

print(myH1)  #findALL包含了 括号 不能 print string了

for i in myH1:
    if "这是" in i.string:  #如果 “这是” 字符在 i字符串中
                           # 打印出i 即排除第一个没有这是的h1
        print(i.string)