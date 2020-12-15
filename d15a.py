import sys
data = sys.stdin.read().strip().split('\n')

a = list(map(int, data[0].split(',')))
last = [-1]*3000
for i in range(2020):
	if i >= len(a):
		if last[a[i-1]] == -1:
			a.append(0)
		else:
			a.append(i-1-last[a[i-1]])
	last[a[i-1]] = i-1
	# print(a[i])

print(a[-1])