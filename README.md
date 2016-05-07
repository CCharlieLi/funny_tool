Funny tools for downloading movies and BLEACH comics
-----------------

- Introduction
   - Automatically download movie links of latest movies from 电影天堂(http://www.ygdy8.net).
   - No link will be downloaded twice according to latest id in log file(DYTT.txt).
   - Automatically download latest comics BLEACH from __BLEACH__ __Baidu__ __Tieba__.
   - Comics will be saved in __BLEACH/[Name]__ in current directory.
   - No comics will be downloaded twice according to existence of __BLEACH/[Name]__.

- Usage

```
pip install funny_tool
```

```
usage: funny_tool [-h] [-b] [-d] [-p PAGE]

optional arguments:
  -h, --help            show this help message and exit
  -b, --bleach          Download BLEACH.
  -d, --dytt            Download latest movies from dytt.
  -p PAGE, --page PAGE  pages to retrieve when downloading movies from dytt,
                        should be used with -d.
```

### License

MIT

