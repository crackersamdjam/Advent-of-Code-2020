import re, sys
data = sys.stdin.read().split('\n')

d = dict()

for s in data:
	s = s.strip('.').split(',')
	t = s[0].split()
	a = t[0]+t[1]

	s[0] = s[0][len(a)+15:]
	for i in s:
		t = i.split()
		if t[0] == 'no':
			break
		n = int(t[0])
		b = t[1]+t[2]

		if b not in d:
			d[b] = list()
		if a not in d:
			d[a] = list()
		d[a].append([n, b])

def go(a):
	sz = 1
	for n, b in d[a]:
		sz += n*go(b)
	return sz

print(go('shinygold')-1)
