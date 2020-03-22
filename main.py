#!/usr/bin/env python

import argparse
import json
import logging
import time

from collections import defaultdict

users= defaultdict(list)

if __name__ == '__main__':
	fd= open("../_chat.txt",mode='r',encoding='utf8', newline='\r\n')
	for i, line in enumerate(fd):   
		date = line.split(",")[0].split("[")[1]
		time = line.split(",")[1].split("]")[0]
		user = line.split("]")[1].split(":")[0].strip()
		message = line.split("]")[1].split(":")[1]
		users[user].append((date, time, message))
	print(users)
	fd.close()
