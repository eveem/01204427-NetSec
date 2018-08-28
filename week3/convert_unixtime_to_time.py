from datetime import datetime

fn = open('login_unixtime.txt', 'r')

hour_data = {}

for line in fn:
    ts = int(line)
    ts /= 1000.0
    x = datetime.fromtimestamp(ts).strftime('%H')
    x += '.00'
    if x in hour_data:
        hour_data[x] += 1
    else:
        hour_data[x] = 1

hour_data_l = sorted(hour_data)
print(hour_data_l)

x = []
for i in hour_data_l:
    x.append(hour_data[i])

print(x)