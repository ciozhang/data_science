import sys
from datetime import datetime
count = 0
total_sales = 0
for line in sys.stdin:
	data = line.strip().split('\t')
	weekday = datetime.strptime(data[0], "%Y-%m-%d").weekday()
	sales = float(data[4])
	if weekday == 6:
		total_sales += sales
		count += 1
print(total_sales/count)