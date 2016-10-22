#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

class RRYS_Login(object):
    
    def __init__(self):
        self.prefix = "http://www.zimuzu.tv"
        self.sess = requests.session()
        self.data = {
            "account": "ccharlieli",
            "password": "!Q@W#E",
            "remember": "1",
            "url_back": ""
            }
        
    def getSession(self):
        self.sess.get(self.prefix)
        self.sess.post("http://www.zimuzu.tv/User/Login/ajaxLogin", self.data)
        return self.sess
