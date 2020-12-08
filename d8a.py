import sys
data = sys.stdin.read().split('\n')

st = set()
val = 0
i = 0
while 1:
	if i in st:
		break
	st.add(i)
	s = data[i].split()
	if s[0] == 'acc':
		val += int(s[1])
		i += 1
	elif s[0] == 'jmp':
		i += int(s[1])
	else:
		i += 1

print(val)