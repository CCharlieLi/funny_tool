from .bleach import BLEACH
from .dytt import DYTT
from .shield import SHIELD

def bleach():
    b = BLEACH()
    b.get_Latest_URLs()

def dytt(page = 1):
    d = DYTT()
    d.get_Latest_URLs(page)

def shield():
	s = SHIELD()
	s.get_serials()
