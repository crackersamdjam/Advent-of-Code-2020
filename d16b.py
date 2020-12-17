import sys, itertools

att = []
#d16b_input.txt already has invalid tickets filtered out

while 1:
	s = input()
	if not s:
		break
	name, s = s.split(':')
	s = s.split('or')
	req = []
	for i in s:
		a, b = map(int, i.strip().split('-'))
		# print(a, b)
		req.append([a, b])
	att.append([name, req])

# your ticket
input()
mine = list(map(int, input().split(',')))
tickets = [mine]
ans = 1

input()
input()

while 1:
	try:
		s = input()
	except:
		break
	a = list(map(int, s.split(',')))
	tickets.append(a)

rem = list(range(len(att)))

while len(rem):
	# try to find the only possible att for this i
	for i in rem:
		pos = []
		# list of possible ones
		for cur in att:
			ok = 1
			for j in tickets:
				found = 0
				for interval in cur[1]:
					if interval[0] <= j[i] <= interval[1]:
						found = 1
						break

				if not found:
					ok = 0
					break
			if ok:
				pos.append(cur)

		assert len(pos) > 0
		if len(pos) == 1:
			# remove this one
			# print('rm', i, pos[0][0])
			# sys.stdout.flush()
			if pos[0][0].startswith('departure'):
				ans *= mine[i]
			rem.remove(i)
			att.remove(pos[0])

print(ans)