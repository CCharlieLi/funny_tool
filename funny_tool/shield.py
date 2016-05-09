#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from tqdm import tqdm
from utils.rrys_login import RRYS_Login
import urllib, sys, os, time
reload(sys)
sys.setdefaultencoding( "utf-8" )

class SHIELD(object):

    def __init__(self):
        self.prefix = 'http://www.zimuzu.tv/'
        self.type = 'HR-HDTV'
        self.logfile = 'SHIELD.txt'
        self.link = ['迅雷'] # '电驴','网盘','城通'

    '''
    Calculate shows to download
    '''
    def calculate(self, list, last = 'S00E00'):
        last_index = -1
        latest_index = len(list) - 1
        for each in list:
            if self.extract_string(each.find_all('div')[0].a.contents[0]) == last:
                last_index = list.index(each)
        return latest_index - last_index

    '''
    Extract 'S.H.I.E.L.D.'     TOTD: should replace with regex.
    '''
    def extract_string(self, string):
        return string[string.find("S.H.I.E.L.D.") + 12: string.find("S.H.I.E.L.D.") + 18]

    '''
    Make log file for links
    '''
    def mklog(self):
        cwdir = os.getcwd()
        self.path = cwdir + '/' + self.logfile
        if os.path.exists(self.path):
            return
        else:
            f = open(self.path, 'w')
            f.close()

    '''
    Get info from tv play list
    '''
    def get_serials(self, sersials_id = '30675'):
        # Make log file if not exist
        self.mklog()

        # Get last num
        log = open(self.path, 'r+a')
        try:
            last = self.extract_string(log.readlines()[-(1 + len(self.link))])
            if 'S' not in last and 'E' not in last:
                last = 'S00E00'
        except Exception, e:
            last = 'S00E00'

        # Parse html
        sess = RRYS_Login().getSession()
        data = sess.get(self.prefix + 'resource/list/' + sersials_id).text
        soup = BeautifulSoup(data, 'lxml')
        lists = soup.find_all('li', class_="clearfix", attrs={"format": self.type})

        count = self.calculate(lists, last)
        print count
        # Define progress bar's length
        progress_bar = tqdm(unit='link', total=count)

        for each in lists:
            divs = each.find_all('div')
            name = divs[0].a.contents[0]
            size = divs[0].font.contents[0]

            if self.extract_string(name) > last:
                log.write('\n' + time.ctime() + ' - ' + name + '   ' + size + '\n')
                for a in divs[1].find_all('a'):
                    link_type = a.contents[0]
                    if link_type not in self.link:
                        continue

                    if link_type == '电驴' or link_type == '网盘' or link_type == '城通':
                        log.write('-*-' + link_type + ':  ' + a.get('href') + '\n')
                    elif link_type == '迅雷':
                        log.write('-*-' + link_type + ':  ' + a.get('thunderhref') + '\n')
                progress_bar.update(1)
        
        log.close()
         # Close bar
        progress_bar.close()
        print('SHIELD: Download finished!  ' + str(count) + ' tv serials downloaded. Check SHIELD.txt.')
