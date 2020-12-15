import sys, math
data = sys.stdin.read().strip().split('\n')

x = 0
y = 0
mx = [1, 0, -1, 0]
my = [0, 1, 0, -1]
d = 0

for s in data:
	op = s[0]
	v = int(s[1:])
	if op == 'N':
		y += v
	elif op == 'S':
		y -= v
	elif op == 'E':
		x += v
	elif op == 'W':
		x -= v
	elif op == 'F':
		x += v*mx[d]
		y += v*my[d]
	elif op == 'R':
		d = (d-v//90)%4
	elif op == 'L':
		d = (d+v//90)%4
	else:
		sys.exit(1)

print(abs(x)+abs(y))