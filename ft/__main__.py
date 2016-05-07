from .BLEACH import BLEACH
from .DYTT import DYTT
import argparse

b = BLEACH()
b.get_Latest_URLs()

parser = argparse.ArgumentParser(description="parameters error")
parser.add_argument('-page',action="store",dest="page",type=int,required=False)
given_args = parser.parse_args()
page = given_args.page

t = DYTT()
if page == None:
    page = 1

t.get_Latest_URLs(page)
