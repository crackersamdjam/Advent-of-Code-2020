import sys
s = sys.stdin.read().split()
n = len(s)
m = len(s[0])

ans = 0
y = 0
for x in range(n):
	if s[x][y] == '#':
		ans += 1
	y = (y+3)%m

print(ans)