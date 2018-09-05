# f = open('35_egress_path.txt', 'r')
f = open('36_ingress_path.txt', 'r')
dc ={'unk': 0}

for line in f:
    x = line.split('?')
    x = x[0]
    x = x.replace('\n', '')
    x = x.split('/')
    new = []
    for j in x:
        if '.' in j:
            new.append(j)
    # print(new)
    if new:
        new = new[-1].lower()
        new = new.split('.')
        new = new[-1]
        if new in dc:
            dc[new] += 1
        else:
            dc[new] = 1
    else:
        dc['unk'] += 1

import operator
sorted_d = sorted(dc.items(), key=operator.itemgetter(1))

for i in sorted_d:
    print(i)

# import os
# for line in f:
#     filename, file_extension = os.path.splitext(line)
#     print(file_extension, filename)