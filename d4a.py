import sys
data = sys.stdin.read().split('\n')

ans = 0
vals = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
# 'cid' not required

cur = []
for s in data:
	s = s.split()
	if not s:
		cnt = 0
		for v in vals:
			cnt += cur.count(v) > 0
		ans += cnt == len(vals)
		cur.clear()
	else:
		for i in s:
			cur.append(i.split(':')[0])

print(ans)