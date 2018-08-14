import csv
import json
import random

nodes = []
edges = []
id2name = {}
id2size = {}

TH = 30

csvfile = open('./internal_data_rowname.csv', 'r')
reader = csv.DictReader(csvfile)
for row in reader:
    id2name[row['current']] = row['name']
    val = float(row['bandwidth'])/TH
    if row['current'] not in id2size:
        id2size[row['current']] = val
    else:
        id2size[row['current']] += val
    if row['source'] not in id2size:
        id2size[row['source']] = val
    else:
        id2size[row['source']] += val
    
    edge = {}
    edge['sourceID'] = row['source']
    edge['targetID'] = row['current']
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

nodes = sorted(nodes, key=lambda k: k['size'], reverse=True) 

d = {}
d['nodes'] = nodes
d['edges'] = edges

data = json.dumps(d)
with open('./data.json', 'w') as f:
    f.write(data)
