import urllib.request
from bs4 import BeautifulSoup
import os
from tqdm import tqdm

class DYTT(object):
    
    def __init__(self):
        self.prefix = 'http://www.ygdy8.net'
        self.logfile = 'DYTT.txt'
        self.path = os.getcwd() + '/' + self.logfile

    '''
    Get link from movie page
    '''
    def get_FTP(self, source_url):
        source_url = self.prefix + source_url
        
        # Open URL and get DOM
        data = urllib.request.urlopen(source_url).read().decode('gb2312', 'ignore')

        # Find characters
        soup = BeautifulSoup(data, 'lxml')
        ftp_link = soup.find('td', {'bgcolor': '#fdfddf'}).contents[0]['href']
        return str(ftp_link)

    ''' 
    Get movies info from each page
    '''
    def get_Latest_URLs(self, page = 1):
        # Get latest num
        log = open(self.path, 'a+')
        log.seek(0)
        try:
            latest = int(log.readlines()[-1])
        except:
            latest = 0

        count = 0
        for each in range(1,page+1)[::-1]:
            index_url='/html/gndy/dyzz/list_23_' + str(each) + '.html'
            print('Downloading page: ' + str(each))
            index_url = self.prefix + index_url

            # Define progress bar's length
            progress_bar = tqdm(unit='link', total=25)

            # Parse html
            data = urllib.request.urlopen(index_url).read().decode('gb2312', 'ignore')
            soup = BeautifulSoup(data, 'lxml')
            lists = soup.findAll('a', {'class': 'ulink'})
            
            for each in lists[::-1]:
                latest_num = int(each['href'].split('/')[-1].split('.')[0])
                if latest < latest_num:
                    link = each['href']
                    log.write(self.get_FTP(link)+'\n')
                    latest = latest_num
                    count = count + 1
                    progress_bar.update(1)
            
            # Write latest
            log.write(str(latest)+'\n')
            # Close bar
            progress_bar.close()

        log.close()
        if count == 0:
            print('DYTT: No new movies to download since last time.')
        print('DYTT: Download finished!  ' + str(count) + '  movies downloaded. Check DYTT.txt.')
