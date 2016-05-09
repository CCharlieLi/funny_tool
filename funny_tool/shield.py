#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from utils.rrys_login import RRYS_Login

class SHIELD(object):

    def __init__(self):
        self.prefix = 'http://www.zimuzu.tv/'
        
    def get_serials(self, sersials_id = '30675'):
        sess = RRYS_Login().getSession()
        soup = BeautifulSoup(sess.get(self.prefix + 'resource/list/' + sersials_id).text)
        lists = soup.find_all('li', class_="clearfix", attrs={"format": "HR-HDTV"})
        print(lists)
s = SHIELD()
s.get_serials()