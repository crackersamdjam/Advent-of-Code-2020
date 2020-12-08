import sys
s = [i.split() for i in sys.stdin.read().split('\n')]

def run():
	st = set()
	val = 0
	i = 0
	while i < len(s):
		if i in st:
			return [False, 0]
		st.add(i)
		if s[i][0] == 'acc':
			val += int(s[i][1])
			i += 1
		elif s[i][0] == 'jmp':
			i += int(s[i][1])
		else:
			i += 1
	return [True, val]

for i in range(len(s)):
	if s[i][0] == 'jmp':
		s[i][0] = 'nop'
		if run()[0]:
			print(run()[1])
			break
		s[i][0] = 'jmp'

	if s[i][0] == 'nop':
		s[i][0] = 'jmp'
		if run()[0]:
			print(run()[1])
			break
		s[i][0] = 'nop'
