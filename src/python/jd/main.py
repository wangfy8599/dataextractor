# -*- coding:utf-8 -*-
import urllib
import urllib.parse
import json
from pyquery import PyQuery
import requests
import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def get_jd(keyword):
    jd_search_url = 'https://search.jd.com/Search?keyword={}&enc=utf-8'.format(urllib.parse.quote(keyword))
    r = requests.get(jd_search_url, headers=headers)
    print(r.url)
    print(r.encoding)
    #print(resp_r.history)
    #print(resp_r.headers)
    r_text = r.text.encode(r.encoding).decode('utf-8')
    #print(r_text)
    doc = PyQuery(r_text)

    elements = doc(".gl-i-wrap")

    print(str(elements))

    for obj in elements:
        product = {}
        product["price"] = PyQuery(obj)(".p-price").text()
        product["name"] = PyQuery(obj)(".p-name").text()
        product["href"] = PyQuery(obj)(".p-name")("a").attr("href")
        product["comment"] = PyQuery(obj)(".p-commit").text()
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
#get_baidu(keyword)
