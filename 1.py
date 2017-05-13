#!/usr/bin/python
import sys
from datetime import datetime

for line in sys.stdin:
	data = line.strip().split('\t')
	weekday = datetime.strptime(data[0], "%Y-%m-%d").weekday()
	sales = data[4]
	print('{}\t{}'.format(weekday, sales))