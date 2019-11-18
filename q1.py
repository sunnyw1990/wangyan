# -*- coding: utf-8 -*-
"""
Created on 2019-11-17
@author: wangy
"""

import requests
from pyquery import PyQuery as pq


def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except Exception:
        return ""


def main():
    print("start")
    url = 'http://www.baidu.com/s?wd=王艳'
    doc = pq(getHtml(url))
    for li in doc('#content_left h3.t a').items():
        print(u'标题：%s' % li.text())
        print(u'链接：%s' % li.attr('href'))
    print("end")


if __name__ == '__main__':
    main()
