from datetime import datetime
import json

fn = open('login-20170102-anon.csv', 'r')

data = {}

for line in fn:
    x = line.split(' ')
    if x[0] in data:
        data[x[0]].append(x[1])
        data[x[0]].append(x[3])
    else:
        data[x[0]] = [x[1], x[3]]

time = {}
basket = [0] * 1440

for i in data:
    temp = data[i]
    if temp[1] == '-' and len(temp) == 4:
        st = int(temp[0])/1000.0
        h = datetime.fromtimestamp(st).strftime('%H')
        m = datetime.fromtimestamp(st).strftime('%M')
        st = int(h)*60 + int(m)

        ed = int(temp[3])/1000.0
        h = datetime.fromtimestamp(ed).strftime('%H')
        m = datetime.fromtimestamp(ed).strftime('%M')
        ed = int(h)*60 + int(m)

        for j in range(st, ed + 1):
            basket[j] += 1

dataout = []

for i in range(0, 1440):
    if i % 15 == 0:
        # dataout.append(basket[i])
        x = str(int(i/60)).zfill(2) + ':' + str(i%60).zfill(2)
        # labelout.append(str(int(i/60)).zfill(2) + ':' + str(i%60).zfill(2))
        dataout.append([x, basket[i]])

data = json.dumps(dataout)
with open('user_time.json', 'w') as f:
    f.write(data)