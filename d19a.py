import sys, re
# data = sys.stdin.read().strip().split('\n')
input = sys.stdin.readline
ans = 0
q = ['' for i in range(200)]
dp = ['' for i in range(200)]

def go(i):
	if dp[i] or not len(q[i]):
		return dp[i]
	if q[i][0] == '\"':
		assert len(q[i]) == 3
		dp[i] = q[i][1]
		return dp[i]
	q[i] = q[i].split(' ')
	dp[i] = '('
	for j in q[i]:
		if j == '|':
			dp[i] += '|'
		else:
			assert int(j) != i
			dp[i] += go(int(j))
	dp[i] += ')'
	return dp[i]

while 1:
	s = input().strip()
	if len(s) == 0:
		break
	s = s.split(':')
	q[int(s[0])] = s[1][1:]

while 1:
	s = input().strip()
	if len(s) == 0:
		break
	if re.fullmatch(go(0), s):
		ans += 1

print(ans)