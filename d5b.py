import re, sys
data = sys.stdin.read().split('\n')
a = []

for s in data:
	v = 0
	for c in s:
		v *= 2
		if c == 'B' or c == 'R':
			v += 1
	a.append(v)

a.sort()
a.pop(0)
for i in range(len(a)):
	if a[i]-a[0] != i:
		print(a[i-1]+1)
		break