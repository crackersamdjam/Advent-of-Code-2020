import sys
data = sys.stdin.read().strip().split('\n')

def go(a, b):
	vis = set()
	while 1:
		if len(a) == 0:
			return 1
		if len(b) == 0:
			return 0

		l = (tuple(a), tuple(b))
		if l in vis:
			return 0
		vis.add(l)

		ac = a.pop(0)
		bc = b.pop(0)

		if len(a) >= ac and len(b) >= bc:
			win = go(a[:ac], b[:bc])
		else:
			win = 0 if ac > bc else 1
		
		if win == 0:
			a.append(ac)
			a.append(bc)
		else:
			b.append(bc)
			b.append(ac)

a = []
b = []

for s in data:
	if len(s) == 0:
		continue
	if s[0] == 'P':
		a, b = b, a
		continue
	b.append(int(s))

go(a, b)
if len(b) == 0:
	b = a

ans = 0
for i in range(1, len(b)+1):
	ans += i*b[-i]

print(ans)