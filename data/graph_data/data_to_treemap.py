# f = open('312_userlist.txt')
# f = open('33_egress_hostname.txt')
# f = open('34_ingress_hostname.txt')

l = []

for line in f:
	x = line.replace('\n', '')
	x = x.split(' ')
	x = x[-2:]
	l.append({'name': x[1], 'value': int(x[0])})

print(l)