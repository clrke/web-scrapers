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
	first = True
	file_output.write("[\n")
	for subject in subjects:

		for key, value in subject.items():
			subject[key] = re.sub(r'\n *', ' ', value)

		if first:
			file_output.write("\t{\n")
		else:
			file_output.write(",\n\t{\n")

		file_output.write('\t\t"%s": "%s",\n' % ('code', subject['code']))
		file_output.write('\t\t"%s": "%s",\n' % ('description', subject['description']))
		file_output.write('\t\t"%s": "%s",\n' % ('section', subject['section']))
		file_output.write('\t\t"%s": "%s",\n' % ('lec', subject['lec']))
		file_output.write('\t\t"%s": "%s",\n' % ('lab', subject['lab']))
		file_output.write('\t\t"%s": "%s",\n' % ('units', subject['units']))
		file_output.write('\t\t"%s": "%s"\n' % ('schedule', subject['schedule']))

		if first:
			file_output.write("\t}")
			first = False
		else:
			file_output.write("\t}")

	file_output.write("\n]\n")
