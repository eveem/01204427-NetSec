import csv
import json
import random
from math import log

nodes = []
edges = []
id2name = {}
id2size = {}

# csvfile = open('./international_data.csv', 'r')
csvfile = open('./domestic_data.csv', 'r')
reader = csv.DictReader(csvfile)
for row in reader:
    id2name[row['ASN']] = row['Name']
    val = log(float(row['Bandwidth']), 2)
    if row['ASN'] not in id2size:
        id2size[row['ASN']] = val
    else:
        id2size[row['ASN']] += val
    if row['ASN-Source'] not in id2size:
        id2size[row['ASN-Source']] = val
    else:
        id2size[row['ASN-Source']] += val
    
    edge = {}
    edge['sourceID'] = row['ASN-Source']
    edge['targetID'] = row['ASN']
    edge['size'] = 1
    edge['attributes'] = {}
    edges.append(edge)

r = lambda: random.randint(0, 255)
id2color = {}

for idx in id2name:
    id2color[idx] = '#%02X%02X%02X' % (r(), r(), r())
    
for idx in id2name:
    node = {}
    node['id'] = idx
    node['label'] = id2name[idx]
    node['color'] = id2color[idx]
    node['size'] = id2size[idx]
    node['x'] = random.uniform(-1000, 1000)
    node['y'] = random.uniform(-1000, 1000)
    node['attributes'] = {}
    nodes.append(node)

nodes = sorted(nodes, key=lambda k: k['x'], reverse=True) 

d = {}
d['nodes'] = nodes
d['edges'] = edges

data = json.dumps(d)
# with open('./international_data.json', 'w') as f:
#     f.write(data)
with open('./domestic_data.json', 'w') as f:
    f.write(data)
