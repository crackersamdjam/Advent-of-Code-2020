import sys, math
data = sys.stdin.read().strip().split('\n')

mask = 'X'*36
d = dict()

for s in data:
	s = s.split()
	if s[0] == 'mask':
		mask = s[2]
	else:
		n = "{0:b}".format(int(s[0][4:-1]))
		n = ('0'*36+n)[-36:]
		v = int(s[2])
		delta = 0
		for j in range(36):
			if mask[j] == '1':
				n = n[:j]+'1'+n[j+1:]
			elif mask[j] == 'X':
				n = n[:j]+'0'+n[j+1:]
				delta |= 1<<(35-j)
		n = int(n, 2)
		j = delta
		while 1:
			d[j|n] = v
			if j == 0:
				break
			j -= 1
			j &= delta

ans = 0
for i in d:
	ans += d[i]
print(ans)