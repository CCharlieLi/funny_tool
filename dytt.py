#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2,BeautifulSoup
import re,time

class dytt(object):

    def __init__(self):
        self.prefix = "http://www.ygdy8.net"

    def get_FTP(self, source_url):
        source_url = self.prefix + source_url
        
        ''' open URL and get DOM '''

        data = urllib2.urlopen(source_url).read().decode('gb2312', 'ignore')
        data.encode('utf8')

        ''' find characters '''

        soup = BeautifulSoup.BeautifulSoup(data)
        ftp_link = soup.find('td', {"bgcolor": "#fdfddf"}).contents[0]["href"]

        #print ftp_link
        #''' find ftp with re '''
        #try:
        #    res = re.compile(r'(ftp://.*?\.rmvb)')
        #    ftp_link = str(res.findall(str(data))[0]).decode('utf-8')
        #except Exception, e:
        #    res = re.compile(r'(ftp://.*?\.mkv)')
        #    ftp_link = str(res.findall(str(data))[0]).decode('utf-8')

        return str(ftp_link.encode('utf8'))


    ''' first page only for now '''

    def get_Latest_URLs(self, index_url="/html/gndy/dyzz/index.html"):

        index_url = self.prefix + index_url

        data = urllib2.urlopen(index_url).read().decode('gbk', 'ignore')
        data.encode('utf-8')

        soup = BeautifulSoup.BeautifulSoup(data)
        lists = soup.findAll('a', {"class": "ulink"})

        ''' read latest from file '''

        log = open("dytt_log.txt","r+a")
        try:
            latest = int(log.readlines()[-1])
        except Exception, e:
            latest = 44777

        log.write("\n"+time.asctime(time.localtime(time.time()))+"\n")
        for each in lists[::-1]:
            if latest < int(each["href"].split("/")[-1].split(".")[0]):
                name = each.string
                link = each["href"]
                #print isinstance(name, unicode) 
                log.write(name.encode('utf8')+"\n")
                #log.write(link+"\n")
                log.write(self.get_FTP(link)+"\n")

                latest = int(each["href"].split("/")[-1].split(".")[0])
        
        ''' write latest '''   

        log.write(str(latest)+"\n")
        log.close()


if __name__ == '__main__':
    t=dytt()
    t.get_Latest_URLs()



