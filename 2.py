#!/usr/bin/python
import sys
count = 0
total_sales = 0
for line in sys.stdin:
	data = line.strip().split('\t')
	weekday = data[0]
	sales = float(data[1])
	
	if weekday == '6':
		total_sales += sales
		count += 1
print(total_sales/count)