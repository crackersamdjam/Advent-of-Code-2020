import sys, math
data = sys.stdin.read().strip().split('\n')

ang = 0
x = 0
y = 0
dx = 10
dy = 1

for s in data:
	op = s[0]
	v = int(s[1:])
	if op == 'N':
		dy += v
	elif op == 'S':
		dy -= v
	elif op == 'E':
		dx += v
	elif op == 'W':
		dx -= v
	elif op == 'F':
		x += v*dx
		y += v*dy
	elif op == 'L':
		for _ in range(v//90):
			dx, dy = -dy, dx
	elif op == 'R':
		for _ in range(v//90):
			dx, dy = dy, -dx
	else:
		sys.exit(1)
	# print(x, y, dx, dy)

print(abs(x)+abs(y))