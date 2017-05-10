import sys
count = 0
for line in sys.stdin:
	data = line.strip().split(' ')
	if data[6] == "/assets/js/the-associates.js":
		count +=1
print(count)