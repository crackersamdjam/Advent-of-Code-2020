import sys
data = sys.stdin.read().split('\n')
v = []

for i in range(len(data)):
	a = int(data[i])
	v.append(a)
	if i >= 25:
		ok = 0
		for j in range(i-25, i):
			for k in range(i-25, j):
				if v[j]+v[k] == a:
					ok = 1
		if not ok:
			print(a)
			break