#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib,urllib2,BeautifulSoup
import os,re,time,argparse

class BLEACH(object):
    """docstring for BLEACH"""
    def __init__(self):
        self.prefix = "http://tieba.baidu.com"

    def mkdir(self,name):
        cwdir = os.getcwd()
        path = cwdir+"/BLEACH/" + name

        if not os.path.exists(path):
            os.makedirs(path)
            self.path = path
            return True
        else:
            return False

    def cbk(self,a, b, c): 
        '''
        @a: 已经下载的数据块
        @b: 数据块的大小
        @c: 远程文件的大小
        ''' 
        per = 100.0 * a * b / c 
        if per > 100: 
            per = 100 
        print '%.2f%%' % per

    def get_Comics(self,name,comic_url):
        comic_url = self.prefix + comic_url

        if self.mkdir(name):

            data = urllib2.urlopen(comic_url).read().decode('utf-8', 'ignore')
            data.encode('utf-8')

            soup = BeautifulSoup.BeautifulSoup(data)
            lists = soup.findAll('img', {"class": "BDE_Image"})

            count = 0
            for each in lists:
                print "Downloading pic "+str(count)
                pic_url = each["src"]
                urllib.urlretrieve(pic_url,self.path+"/"+str(count)+"."+pic_url.split(".")[-1],self.cbk)
                count = count + 1

            print "Download finished! Check BLEACH folder and have fun!"

        else:
            print "Folder \"BLEACH/" + name.encode('utf8') + "\" already exists! No Downloading operation!"



    def get_Latest_URLs(self,index_url="/f?kw=%CB%C0%C9%F1&fr=ala0"):
        index_url = self.prefix + index_url
        #print index_url
        data = urllib2.urlopen(index_url).read().decode('utf-8', 'ignore')
        data.encode('utf-8')

        soup = BeautifulSoup.BeautifulSoup(data)
        lists = soup.findAll('a', {"class": "j_th_tit"})

        for each in lists:
            name = each["title"].encode('utf8')
            if "★★★" in name and "bleach" in name and "【漫画】" in name:
                self.get_Comics(each["title"],each["href"])
        
if __name__ == "__main__":
    b = BLEACH()
    b.get_Latest_URLs()