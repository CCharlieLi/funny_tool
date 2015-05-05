#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2,BeautifulSoup
import re,time,argparse

class BLEACH(object):
    """docstring for BLEACH"""
    def __init__(self):
        self.prefix = "http://tieba.baidu.com"

    def get_Latest_URLs(self,index_url="/f?kw=%CB%C0%C9%F1&fr=ala0"):
        index_url = self.prefix + index_url
        print index_url
        data = urllib2.urlopen(index_url).read().decode('gb2312', 'ignore')
        data.encode('utf8')
        print data

        soup = BeautifulSoup.BeautifulSoup(data)
        lists = soup.findAll('a', {"class": "j_th_tit"})

        #print lists[1]["title"]
        
if __name__ == "__main__":
    b = BLEACH()
    b.get_Latest_URLs()