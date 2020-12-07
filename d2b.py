ans = 0
for _ in range(1000):
	a, b, c = input().split()
	l, r = map(int, a.split('-'))
	if (c[l-1] == b[0]) ^ (c[r-1] == b[0]):
		ans += 1
print(ans)