import sys
data = sys.stdin.read().split('\n')
v = []
s = 0
val = 177777905

l = 0
r = -1
while 1:
	if s == val:
		print(min(v) + max(v))
		break
	if s < val:
		r += 1
		v.append(int(data[r]))
		s += v[-1]
	else:
		s -= v[0]
		v.pop(0)
		l += 1
