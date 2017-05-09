import sys
def reducer():
	Aadhaar_generated = 0
	old_key = None

	for line in sys.stdin:
		data = line.strip().split('\t')
	if len(data) != 2:
		continue
	this_key, count = data
	if old_key and old_key != this_key:
		print ('{}\t{}'.format(old_key,Aadhaar_generated))
		Aadhaar_generated = 0
	old_key = this_key
	Aadhaar_generated += float(count)
	if old_key != None:
		print ('{}\t{}'.format(old_key,Aadhaar_generated))

reducer()