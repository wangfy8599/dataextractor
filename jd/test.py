import requests

from pyquery import PyQuery as pq       #因为PyQuery书写的时候较为复杂所以用pq 代替
url='''https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page='''
num=eval(input("请输入需要查询结果的页数"))           #自定义页数
for ii in range(num):
    url=url+str(2*ii+1)
    r=requests.get(url)
    r.encoding="utf-8"           #这一行必不可少，缺少的话就会出现没有结果的问题
    html=r.text
    print(html)
    print(type(html),len(html))
    text=pq(html)
    divs=text("div").filter(".p-name").items()      #items（）可以让divs 成为可以遍历的类型
    prices=text("div").filter(".p-price").items()   #items（）让pricess 成为可以遍历的类型
    print(type(divs))
    print(type(prices))
    name=[]
    price=[]
    t="{:^5}\t{:6}\t{:^30}"
    for div in divs:
        ems=div("a").attr("title")
        name.append(ems)
    for pricess in prices:
        price.append(pricess("i").text())
    for i in range(len(name)):
        print(t.format((30 * ii) + i + 1, price[i], name[i]))
