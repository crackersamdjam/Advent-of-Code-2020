import sys
data = sys.stdin.read().strip().split('\n')

v = dict()
ans = []

for s in data:
	s = s.split('(')
	a = s[0][:-1]
	b = s[1][9:-1]
	a = set(a.split(' '))
	b = list(x.strip() for x in b.split(','))
	for i in b:
		if i not in v:
			v[i] = a
		else:
			v[i] = v[i].intersection(a)

while len(v):
	rm = 0
	for i in v:
		if len(v[i]) == 1:
			rm = i
			break
	# assert rm != 0
	food = v.pop(rm).pop()
	for i in v:
		if food in v[i]:
			v[i].remove(food)
	ans.append([rm, food])

print(','.join(i[1] for i in sorted(ans)))