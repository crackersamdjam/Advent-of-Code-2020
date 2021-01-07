import sys
data = sys.stdin.read().strip().split('\n')

st = set()

for s in data:
	x = y = 0
	i = 0
	while i < len(s):
		if s[i] == 'e':
			x += 2
		elif s[i] == 'w':
			x -= 2
		elif s[i] == 'n':
			y += 1
			i += 1
			if s[i] == 'e':
				x += 1
			else:
				x -= 1
		else:
			y -= 1
			i += 1
			if s[i] == 'e':
				x += 1
			else:
				x -= 1
		i += 1
	if (x, y) in st:
		st.remove((x, y))
	else:
		st.add((x, y))

print(len(st))