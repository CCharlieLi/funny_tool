#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .bleach import BLEACH
from .dytt import DYTT
import argparse

def All():
    parser = argparse.ArgumentParser(description = "funny_tool: Download movies and comics!")
    parser.add_argument('-b', '--bleach', action="store_true", help="Download BLEACH.")
    parser.add_argument('-d', '--dytt', action="store_true", help="Download latest movies from dytt.")
    parser.add_argument('-p', '--page', action="store", type=int, default=1, 
        help="pages to retrieve when downloading movies from dytt, should be used with -d.")
    given_args = parser.parse_args()

    if given_args.bleach:
        b = BLEACH()
        b.get_Latest_URLs()

    if given_args.dytt:
        t = DYTT()
        t.get_Latest_URLs(given_args.page)

    if given_args.bleach == False and given_args.dytt == False:
        parser.print_help()

def BLEACH():
    b = BLEACH()
    b.get_Latest_URLs()

def DYTT():
    t = DYTT()
    t.get_Latest_URLs(given_args.page)
