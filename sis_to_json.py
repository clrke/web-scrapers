# -*- coding: utf-8 -*-

import sys
import os, re, glob
import json
from bs4 import BeautifulSoup

input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[1])
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[2])

def getSoup(text):
	return BeautifulSoup(text)

html_text = open(input_path).read()

soup = getSoup(html_text).table.tbody

subjects = [];

for tr in soup.find_all("tr", recursive=False):
	year_level = tr.td.table.tbody.tr.td.string.strip()

	print(year_level)

	for tr2 in tr.td.table.tbody.find_all("tr", recursive=False):
		try:
			for subject in tr2.td.table.tbody.find_all("tr", bgcolor="white"):
				columns = subject.find_all("td", recursive=False)
				subjects.append({
					"code": columns[0].string.strip(),
					"description": columns[1].string.strip(),
					"section": columns[2].string.strip(),
					"lec": columns[3].string.strip(),
					"lab": columns[4].string.strip(),
					"units": columns[5].string.strip(),
					"schedule": columns[7].string.strip()
				})
		except:
			pass

with open(output_path, 'w') as file_output:
	file_output.write(json.dumps(subjects, indent=2))
