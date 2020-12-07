import re, sys
data = sys.stdin.read().split('\n')
ans = 0

for s in data:
	v = 0
	for c in s:
		v *= 2
		if c == 'B' or c == 'R':
			v += 1
	ans = max(ans, v)

print(ans)