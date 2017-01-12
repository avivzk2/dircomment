#!/usr/bin/env python3.5.1

import os
import sys
import argparse
import re
import json


PATH = os.path.realpath(__file__).rsplit('/', 1)[0]

DATA_FILE = "{}/{}".format(PATH, 'dir_data.json')
DIR_DISP = """{name} - {comment}"""
ERROR_MSG = """ [ ERROR ] : {}"""


def get_current_path():
	cwd = os.getcwd()
	name = cwd.rsplit('/', 1)[-1]
	return (name, cwd)


def parse_args(args):
	comment = " ".join(args)
	return comment


def create_json_file(file):
	# with open(file, mode='w', encoding='utf-8') as ws:
		# json.dump({}, ws)
	with open(file, 'w') as ws:
		ws.write("{}")


def load_json():
	data = None
	try:
		with open(DATA_FILE) as rs:
			data = json.load(rs)
	except IOError as e:
		print(ERROR_MSG.format(e))
	return data


def add_dir(dir, comment):
	if not os.path.isfile(DATA_FILE):
		create_json_file(DATA_FILE)
	data = dict(load_json())
	entry = {dir: comment}
	data.update(entry)
	try:
		with open(DATA_FILE, mode='w', encoding='utf-8') as ws:
			json.dump(data, ws)
	except IOError as e:
		print(ERROR_MSG.format(e))


def retrieve_dir(cwd):
	data = load_json()
	if not data:
		return "None"
	if not cwd in data:
		print("ERROR")
	return data[cwd]


def main(args):
	name, cwd = get_current_path()
	comment = parse_args(args)
	if comment:
		add_dir(cwd, comment)
	else:
		comment = retrieve_dir(cwd)

	print(DIR_DISP.format(name=name, comment=comment))


if __name__ == '__main__':
	main(sys.argv[1:])
