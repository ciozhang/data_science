import sys
count = 0
popular = {}
for line in sys.stdin:
	line = line.replace('http://www.the-associates.co.uk','')
	data = line.strip().split(' ')
	if 'http://www.the-associates.co.uk' in line:
		print('ok')
		continue
	
	key = data[6]
	if key in popular.keys():
		popular[key] += 1
	else:
		popular[key] = 1
max_count = 0
max_key = None
for key in popular:
	if popular.get(key) > max_count:
		max_count = popular.get(key)
		max_key = key

print(max_key,max_count)