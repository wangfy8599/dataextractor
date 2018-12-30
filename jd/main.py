# -*- coding:utf-8 -*-
import urllib
import urllib.parse
import json
from pyquery import PyQuery
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')


def get_jd(keyword):
    doc = PyQuery('https://search.jd.com/Search?keyword=' + urllib.parse.quote(keyword), encoding="utf-8")
    elements = doc(".gl-i-wrap")

    print(str(elements))

    for obj in elements:
        product = {}
        product["price"] = PyQuery(obj)(".p-price").text()
        product["name"] = PyQuery(obj)(".p-name").text()
        product["href"] = PyQuery(obj)(".p-name")("a").attr("href")
        #print(str(product).decode('string_escape'))
        print(str(product))


def get_baidu(keyword):
    doc = PyQuery('http://www.baidu.com/s?wd=' + urllib.parse.quote(keyword), encoding="utf-8")
    elements = doc(".result")
    for eme in elements:
        obj = json.loads(PyQuery(eme)("div")(".c-tools").attr("data-tools"))
        obj["text"] = PyQuery(eme)(".c-abstract").text()
        print(str(obj))


keyword = '千禾酱油'
get_jd(keyword)
get_baidu(keyword)
