Funny tools for Charlie
-----------------

- dytt.py 
   - Automatically generate FTP links of latest movies on 电影天堂(http://www.ygdy8.net)
   - Movies' names and FTP links are saved in __dytt_log.txt__
   - No link will be downloaded twice according to latest id (last line of __dytt_log.txt__)
   - BeautifulSoup is needed

- BLEACH.py - Automatically download latest comics BLEACH from Baidu tieba.
   - not finished yet


### Usage

- Install [python 2.7](https://www.python.org/downloads/)
- Install BeautifulSoup by:

```shell
sudo pip install beautifulsoup
```

- By default, running the command line below will download links of latest movies(whoes id is greater than last line of dytt_log.txt,or 44777 by default) in index page 1.

```shell
python dytt.py
```

- If you want to download latest movies more than page 1, give it a parameter __page__:

```shell
python dytt.py -page=2
```

- Check the dytt_log.txt for movies' links!

### Author

Charlie(ccharlieli@live.com) 

### License

GPLv3

