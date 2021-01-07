# this can be sped up a bit by ignoring the non-existent cells
import sys
data = sys.stdin.read().strip().split('\n')

sz = 110
cur = [[0 for i in range(sz*2)] for j in range(sz*2)]
m = [(2, 0), (-2, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

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
	cur[x][y] ^= 1

# for i in range(-sz, sz):
# 	for j in range(-sz, sz):
# 		if cur[i][j]:
# 			print(i, j)

def out():
	print(sum(map(sum, cur)))
	for i in range(-sz, sz):
		st = 1
		if i%2:
			print(end=' ')
			st = 0
		for j in range(st-sz, sz, 2):
			print(cur[i][j], end=' ')

		for j in range(1-st-sz, sz, 2):
			assert cur[i][j] == 0

		print()

# out()

for _ in range(100):
	pre = [x[:] for x in cur]
	for i in range(-sz, sz):
		for j in range(-sz, sz):
			cnt = 0
			for d in m:
				cnt += pre[i+d[0]][j+d[1]]
			if pre[i][j] and cnt != 1 and cnt != 2:
				cur[i][j] = 0
			elif not pre[i][j] and cnt == 2:
				cur[i][j] = 1
	# out()

print(sum(map(sum, cur)))