import sys
count = 0
for line in sys.stdin:
	data = line.strip().split(' ')
	if data[0] == "10.99.99.186":
		count +=1
print(count)