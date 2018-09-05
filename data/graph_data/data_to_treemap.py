f = open('312_userlist.txt')

l = []

for line in f:
	x = line.replace('\n', '')
	x = x.split(' ')
	x = x[-2:]
	l.append({'name': x[1], 'value': int(x[0])})

print(l)