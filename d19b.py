import sys, re
# data = sys.stdin.read().strip().split('\n')
input = sys.stdin.readline
ans = 0
q = {}
dp = {}
cnt = {}

def go(i):
	if i not in cnt:
		cnt[i] = 0
		dp[i] = ''
	if cnt[i] > 4:
		return dp[i]
	cnt[i] += 1

	f = q[i][0]
	if f[0] == '\"':
		assert len(f) == 3
		dp[i] = f[1]
		return dp[i]
	s = '('
	for j in q[i]:
		if j == '|':
			s += '|'
		else:
			s += go(int(j))
	s += ')'
	dp[i] = s
	return dp[i]

while 1:
	s = input().strip()
	if len(s) == 0:
		break
	s = s.split(':')
	q[int(s[0])] = s[1][1:].split()

q[8] = '42 | 42 8'.split()
q[11] = '42 31 | 42 11 31'.split()

while 1:
	s = input().strip()
	if len(s) == 0:
		break
	if re.fullmatch(go(0), s):
		ans += 1

print(ans)