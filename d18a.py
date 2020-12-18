import sys, math
data = sys.stdin.read().strip().split('\n')
ans = 0

for s in data:
	st = ['']
	for i in range(len(s)):
		if s[i] == '(':
			st.append('')
		elif s[i] == ')':
			v = str(eval(st[-1]))
			st.pop()
			st[-1] += ' '+v
		else:
			st[-1] += s[i]
		try:
			st[-1] = str(eval(st[-1]))
		except:
			pass
		# print(st)
	# print(st[0])
	ans += eval(st[0])
print(ans)