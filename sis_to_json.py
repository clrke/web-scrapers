# -*- coding: utf-8 -*-

import sys
import os, re, glob
import urllib.request
from bs4 import BeautifulSoup

input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[1])
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[2])

def getSoup(text):
	return BeautifulSoup(text)

html_text = open(input_path).read()

soup = getSoup(html_text).table.tbody

for tr in soup.find_all("tr", recursive=False):
	year_level = tr.td.table.tbody.tr.td.string.strip()

	print(year_level)
