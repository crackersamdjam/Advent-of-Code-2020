import sys
data = sys.stdin.read().strip().split('\n')
a = list(map(int, data))
a.append(0)
a.sort()
a.append(a[-1]+3)

dp = [0]*len(a)
dp[0] = 1

for i in range(1, len(a)):
	dp[i] = 0
	for j in range(max(0, i-3), i):
		d = a[i]-a[j]
		if d <= 3:
			dp[i] += dp[j]

print(dp[-1])