import sys
data = sys.stdin.read().strip().split('\n')
#commented out "your ticket" lines
f = 0
req = []
ans = 0

for s in data:
	if s == 'nearby tickets:':
		f = 1
		continue
	if f == 0:
		# remove attr name
		s = s.split(':')[1]

		# split into allowed
		s = s.split('or')

		# cur = []
		for i in s:
			a, b = map(int, i.strip().split('-'))
			# print(a, b)
			req.append([a, b])
			# cur.append([a, b])
		# req.append(cur)
	else:
		ss = s
		s = list(map(int, s.split(',')))
		invalid = 0
		for i in s:
			ok = 0
			for j in req:
				if j[0] <= i <= j[1]:
					ok = 1
					break
			if not ok:
				ans += i
				invalid = 1
		# if not invalid:
			# print(ss)
		#to use as input for part b 

print(ans)