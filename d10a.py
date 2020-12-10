import sys
data = sys.stdin.read().strip().split('\n')
a = list(map(int, data))
a.append(0)
a.sort()
a.append(a[-1]+3)

d = [0, 0, 0, 0]

for i in range(1, len(a)):
	d[a[i]-a[i-1]] += 1

print(d[1]*d[3])