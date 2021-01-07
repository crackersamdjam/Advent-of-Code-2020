import sys
data = sys.stdin.read().strip().split('\n')
a = list(data[0])
a = [int(x)-1 for x in a]
cur = 0

for _ in range(100):
	# print('cups:', [x+1 for x in a])
	mv = []
	i = cur
	init = a[cur]
	for __ in range(3):
		if i+1 < len(a):
			mv.append(a.pop(i+1))
		else:
			mv.append(a.pop(0))
	
	nx = (init-1+9)%9
	while nx in mv:
		nx = (nx-1+9)%9

	dest = (a.index(nx)+1)%len(a)

	# print('pick up', [x+1 for x in mv])
	# print('cur', cur, init+1)
	# print('dest', nx+1, dest)
	# print()

	for b in mv[::-1]:
		a.insert(dest, b)

	dif = a.index(init)-cur+9
	for _ in range(dif):
		a.append(a.pop(0))

	assert a[cur] == init
	cur = (cur+1)%9

	
print(''.join(str(x+1) for x in a[a.index(0)+1:]) + ''.join(str(x+1) for x in a[:a.index(0)]))
