#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2
from bs4 import BeautifulSoup
import os, re, time, argparse, time, shutil
from tqdm import tqdm

class BLEACH(object):
    
    def __init__(self):
        self.prefix = 'http://tieba.baidu.com'

    '''
    Make dir for comics
    '''
    def mkdir(self, name):
        cwdir = os.getcwd()
        self.path = cwdir + '/BLEACH/' + name
        if os.path.exists(self.path):
            if os.listdir(self.path):
                return False
            else:
                return True
        os.makedirs(self.path)
        return True

    '''
    Get images from specific page
    '''
    def get_Comics(self, name, comic_url):
        if not self.mkdir(name):
            again = ''
            while (1):
                again = str(raw_input('Directory ' + name.encode('utf8') + ' already exists, do you wanna to download again? (Y/N)'))
                if again == 'Y' or again == 'N':
                    break
            if again == 'N':
                print('Folder \'BLEACH/' + name.encode('utf8') + '\' already exists!')
                return
            else:
                shutil.rmtree(self.path)
                self.mkdir(name)

        # Parse html
        page_url = self.prefix + comic_url
        data = urllib2.urlopen(page_url).read().decode('utf-8', 'ignore')
        data.encode('utf-8')
        soup = BeautifulSoup(data, 'lxml')
        lists = soup.findAll('img', {'class': 'BDE_Image'})

        print('Downloading: ' + name.encode('utf8'))
        # Define progress bar's length
        progress_bar = tqdm(unit='Pic', total=len(lists))
        count = 0

        for each in lists:
            pic_url = each['src']
            filename = '%03d.txt' % count  + '.' + pic_url.split('.')[-1]
            urllib.urlretrieve(pic_url, filename = self.path + '/' + filename)
            progress_bar.update(1)
            count = count + 1

        # Close bar
        progress_bar.close()

    '''
    Get anime list from given path
    '''
    def get_Latest_URLs(self, index_url='/f?kw=%CB%C0%C9%F1&fr=ala0'):
        index_url = self.prefix + index_url
        # Parse html
        data = urllib2.urlopen(index_url).read().decode('utf-8', 'ignore')
        data.encode('utf-8')
        soup = BeautifulSoup(data, 'lxml')
        lists = soup.findAll('a', {'class': 'j_th_tit '})

        for each in lists:
            name = each['title'].encode('utf8')
            if ('★★★' in name and 'bleach' in name and '【漫画】' in name) or \
            ('【情报】' in name and '英文全图' in name and '死神bleach' in name):
                self.get_Comics(each['title'],each['href'])

        print('BLEACH: Download finished! Check BLEACH directory.')
        