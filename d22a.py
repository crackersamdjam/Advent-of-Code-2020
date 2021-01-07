import sys
data = sys.stdin.read().strip().split('\n')

a = []
b = []

for s in data:
	if len(s) == 0:
		continue
	if s[0] == 'P':
		a, b = b, a
		continue
	b.append(int(s))

while len(a) > 0 and len(b) > 0:
	ac = a.pop(0)
	bc = b.pop(0)
	if ac > bc:
		a.append(ac)
		a.append(bc)
	else:
		b.append(bc)
		b.append(ac)

if len(b) == 0:
	b = a

ans = 0
for i in range(1, len(b)+1):
	ans += i*b[-i]

print(ans)