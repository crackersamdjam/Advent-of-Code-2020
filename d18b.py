import sys, math
data = sys.stdin.read().strip().split('\n')
ans = 0

for s in data:
	s = '(' + s + ')'
	st = ['']
	for i in range(len(s)):
		if s[i] == '(':
			st.append('')
		elif s[i] == ')':
			ss = st[-1].split('*')
			p = 1
			for v in ss:
				p = p*eval(v)
			st.pop()
			st[-1] += str(p)
		else:
			st[-1] += s[i]
	ans += eval(st[0])
print(ans)