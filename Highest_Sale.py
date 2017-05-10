import sys
max_sales = [0.,0.,0.]

for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 6:
		continue
	name = data[2].replace(' ','_').lower()
	sales = float(data[4])
	if name == 'reno':
		if sales > max_sales[0]:
			max_sales[0] = sales
	elif name == 'toledo':
		if sales > max_sales[1]:
			max_sales[1] = sales
	elif name == 'chandler':
		if sales > max_sales[2]:
			max_sales[2] = sales
	else:
		pass
print(max_sales)
