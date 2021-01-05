# this code is very slow
# can try to speed up by adding only index instead of whole box each time I add to grid[][]

import sys
data = sys.stdin.read().strip().split('\n')

def rot(a):
	b = []
	for i in range(len(a)):
		b.append('')
		for j in range(len(a)):
			b[i] += a[-j-1][i]
	return b

def flip(a):
	return a[::-1]

boxes = []
i = 0
while i < len(data):
	ind = int(data[i][5:-1])
	i += 1
	s = []
	for _ in range(10):
		s.append(data[i])
		i += 1
	i += 1
	boxes.append([ind, s])

sz = round(len(boxes)**0.5)
grid = [[None for i in range(sz)] for j in range(sz)]
used = set()

def go(i, j, ind):
	if j == sz:
		i += 1
		j = 0

	if ind >= 0:
		grid[i][j] = boxes[ind]
		used.add(ind)

	# see if no conflict with above and left
	ok = 1
	if i > 0:
		# above
		for k in range(10):
			if grid[i][j][1][0][k] != grid[i-1][j][1][-1][k]:
				ok = 0
	if j > 0:
		# left
		for k in range(10):
			if grid[i][j][1][k][0] != grid[i][j-1][1][k][-1]:
				ok = 0
	if not ok:
		used.remove(ind)
		return

	if len(used) == len(boxes):
		ans = grid[0][0][0]*grid[0][-1][0]*grid[-1][0][0]*grid[-1][-1][0]
		print(ans)
		# print real image for part 2
		for ii in range(sz):
			for kk in range(1, 9):
				for jj in range(sz):
					print(grid[ii][jj][1][kk][1:-1], end='')
				print()
		exit(0)

	for k in range(len(boxes)):
		if k not in used:
			# try to add
			for __ in range(2):
				for _ in range(4):
					go(i, j+1, k)
					boxes[k][1] = rot(boxes[k][1])
				boxes[k][1] = flip(boxes[k][1])

	if ind >= 0:
		used.remove(ind)

go(0, -1, -1)