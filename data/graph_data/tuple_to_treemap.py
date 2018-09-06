# f = open('35_egress_count.txt')
f = open('36_ingress_count.txt')

l = []

f = list(f)
other = f[:-35]
top = f[-35:]

for i in top:
	x = i.replace('(', '').replace(')', '').replace('\n', '').replace("'", '').replace(' ', '')
	x = x.split(',')
	if x[0] == 'unk':
		l.append({'name': 'unknown', 'value': int(x[-1])})
	else:
		l.append({'name': x[0], 'value': int(x[-1])})

v = 0
for i in other:
	x = i.replace('(', '').replace(')', '').replace('\n', '').replace("'", '').replace(' ', '')
	x = x.split(',')
	v += int(x[-1])

l.append({'name': 'other', 'value': int(v)})

print(l)
