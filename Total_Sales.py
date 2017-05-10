import sys
count = 0
total_sales = 0
for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 6:
		continue
	sales = float(data[4])
	total_sales += sales
	count += 1
print(total_sales,count)