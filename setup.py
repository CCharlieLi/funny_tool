#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='funny_tool',
    version='0.2.3',
    description='The funny tools to download movies and comics',
    author='CCharlieLi',
    author_email='ccharlieli@live.com',
    url='https://github.com/CCharlieLi/funny_tool',
    download_url = 'https://github.com/CCharlieLi/funny_tool/releases',
    keywords = ['download', 'bleach', 'dytt'],
    license='MIT',
    packages=['funny_tool', 'funny_tool.utils'],
    install_requires=['beautifulsoup4', 'tqdm', 'requests', 'lxml'],
    zip_safe=False,
    entry_points = {
        'console_scripts': ['ft=funny_tool.funny_tool:all'],
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Natural Language :: Chinese (Simplified)',
        ],
    )