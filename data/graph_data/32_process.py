from datetime import datetime

f = open('32_topmost.txt', 'r')
data = []
dimset = []
ts = set()
us = set()
ipss = set()
ipds = set()
pds = set()
hs = set()

for line in f:
	x = line.replace('\n', '').split(' ')
	d = []
	t = int(x[0])/1000000.0
	s = datetime.fromtimestamp(t).strftime('%H:%M:%S')
	d.append(s)
	d.append(x[1])
	d.append(x[2])
	d.append(x[3])
	d.append(x[4])
	d.append(x[5])
	data.append(d)
	ts.add(s)
	us.add(x[1])
	ipss.add(x[2])
	ipds.add(x[3])
	pds.add(x[4])
	hs.add(x[5])

dimset.append(list(ts))
dimset.append(list(us))
dimset.append(list(ipss))
dimset.append(list(ipds))
dimset.append(list(pds))
dimset.append(list(hs))

# print(data)
print(dimset)

