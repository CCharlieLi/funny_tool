Funny tools for Charlie
-----------------

###  dytt.py 

- Introduction
   - Automatically generate FTP links of latest movies on 电影天堂(http://www.ygdy8.net).
   - Movies' names and FTP links are saved in __dytt_log.txt__.
   - No link will be downloaded twice according to latest id (last line of __dytt_log.txt__).
   - BeautifulSoup is needed.

- Usage

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
   

### BLEACH.py 

- Introduction
   - Automatically download latest comics BLEACH from __BLEACH__ __Baidu__ __Tieba__.
   - Comics will be saved in __BLEACH/[Name]__ in current directory.
   - No comics will be downloaded twice according to existence of __BLEACH/[Name]__.
   - BeautifulSoup is needed.

- Usage

   - Install [python 2.7](https://www.python.org/downloads/)
   - Install BeautifulSoup by:

```shell
sudo pip install beautifulsoup
```

   - Running the command line below firstly will download all "★★★【漫画】死神bleach[XXX]话★★★" BLEACH comics that appeare on Baidu Tieba's first page.(No comics will be downloaded twice according to existence of __BLEACH/[Name]__.)

```shell
python BLEACH.py 
```

   - Check the __BLEACH/__ for comics!


### Author

Charlie(ccharlieli@live.com) 

### License

GPLv3

