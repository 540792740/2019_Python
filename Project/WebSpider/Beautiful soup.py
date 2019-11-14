#coding=utf-8

import requests
from bs4 import BeautifulSoup

def db():
    url = "https://www.douban.com/group/explore?start=30"
    headers = {
        "User-Agent":"Mozilla/5.0",
        "Cookie":'xxxx'                  #cookie需要自行获取
    }
    ret = requests.get(url,headers = headers)
    return ret.content

soup = BeautifulSoup(db(),'html.parser') #按照html格式解析获取到的数据
print(soup.find_all("a",attrs="title"))  #获取标签tag为a  属性中有title的列表
for i in soup.find_all("a",attrs="title"):
    print(i.attrs["href"])               #获取列表中属性href的值（本实例该值为url连接）
    print(i.attrs["title"])              #获取列表中属性title的值（本实例该值为帖子的标题）
    print(i.get_text())                  #获取该标签下的内容