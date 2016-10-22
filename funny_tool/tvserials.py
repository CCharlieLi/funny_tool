from bs4 import BeautifulSoup
from tqdm import tqdm
from .utils.rrys_login import RRYS_Login
from .utils.TVList import get_list
import os, time, re

class TVSerials(object):

    def __init__(self):
        self.prefix = 'http://www.zimuzu.tv/'
        self.type = 'HR-HDTV'
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
    Extract S??E??
    '''
    def extract_string(self, string):
        try:
            return re.search('(S\d{2}E\d{2})\.', string).groups()[0]
        except:
            return 'S99E99'

    '''
    Get info from tv play list
    '''
    def get_serials(self, sersials_id):
        tvlist = get_list()
        if sersials_id not in tvlist.keys():
            print('No TV serials for such a id.')
            return

        self.logfile = tvlist[sersials_id] + '.txt'
        self.path = os.getcwd() + '/' + self.logfile
        print('TV : Starting to download ' + tvlist[sersials_id])

        # Get last num
        log = open(self.path, 'a+')
        log.seek(0)
        try:
            last = self.extract_string(log.readlines()[-(1 + len(self.link))])
            if 'S' not in last and 'E' not in last:
                last = 'S00E00'
        except:
            last = 'S00E00'

        # Parse html
        sess = RRYS_Login().getSession()
        data = sess.get(self.prefix + 'gresource/list/' + sersials_id).text
        soup = BeautifulSoup(data, 'lxml')
        lists = soup.find_all('li', class_="clearfix", attrs={"format": self.type})

        count = self.calculate(lists, last)
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
        print('TV : Download finished!  ' + str(count) + ' tv serials downloaded. Check ' + self.logfile)
