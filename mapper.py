import sys
def mapper():
	for line in sys.stdin:
		data = line.strip().split(',')
		if len(data) != 12 or data[0] == 'Registrar':
			continue
		print('{}\t{}'.format(data[3],data[8]))
mapper()