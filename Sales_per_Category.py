#!/usr/bin/python
import sys

t_s = 0.
c_s = 0.
for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 6:
		continue
	categories, sales = data[3], data[4]
	categories = categories.replace(' ','_').lower()
	if categories == 'toys':
		t_s += float(sales)
	if categories == 'consumer_electronics':
		c_s += float(sales)
print(t_s)
print(c_s)







