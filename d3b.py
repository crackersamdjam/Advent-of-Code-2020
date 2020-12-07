import sys
s = sys.stdin.read().split()
n = len(s)
m = len(s[0])

ans = 1
lx = [1, 1, 1, 1, 2]
ly = [1, 3, 5, 7, 1]
for i in range(5):
	y = 0
	cnt = 0
	for x in range(0, n, lx[i]):
		if s[x][y] == '#':
			cnt += 1
		y = (y+ly[i])%m
	ans *= cnt

print(ans)