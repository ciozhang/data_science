import sys
count = 0
for line in sys.stdin:
	data = line.strip().lower()
	for i in '.,!?:;"()<>[]#$=-/':
		data = data.replace(i,' ')
	text = data.strip().split(' ')
	#print(text)
	for i in text:
		if i == 'fantastic':
			cuont += 1
		if i == 'fantastically':
			print(text[0])
			if text[0] == 'p':
				print(line)
print(count)