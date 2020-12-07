ans = 0
for _ in range(1000):
	a, b, c = input().split()
	l, r = map(int, a.split('-'))
	cnt = c.count(b[0])
	if l <= cnt <= r:
		ans += 1
print(ans)