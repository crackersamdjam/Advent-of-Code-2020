import sys, math
data = sys.stdin.read().strip().split('\n')

mask = 'X'*36
d = dict()

for s in data:
	s = s.split()
	if s[0] == 'mask':
		mask = s[2]
	else:
		n = int(s[0][4:-1])
		v = "{0:b}".format(int(s[2]))

		v = ('0'*36+v)[-36:]
		# print(n, v)
		for j in range(36):
			if mask[j] != 'X':
				v = v[:j]+mask[j]+v[j+1:]
		# print(v)
		d[n] = v;

ans = 0
for i in d:
	# print(i, int(d[i], 2))
	ans += int(d[i], 2)
print(ans)