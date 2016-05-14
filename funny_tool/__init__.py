from .bleach import BLEACH
from .dytt import DYTT
from .tvserials import TVSerials
from .utils.TVList import get_list

def bleach():
    b = BLEACH()
    b.get_Latest_URLs()

def dytt(page = 1):
    d = DYTT()
    d.get_Latest_URLs(page)

# id: String
def tv(id):
	s = TVSerials()
	s.get_serials(id)

def tvlist():
	return get_list()
