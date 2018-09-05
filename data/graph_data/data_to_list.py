f = open('311_request.txt', 'r')

data = []

for line in f:
	x = line.replace('\n', '')
	x = x.split(' ')
	data.append(x[-2])

time = []
for i in range(0, 60):
	time.append('03:' + str(i).zfill(2))

# print(data)
print(time)