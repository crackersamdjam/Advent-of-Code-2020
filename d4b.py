import re, sys
data = sys.stdin.read().split('\n')
ans = 0
cur = dict()

for s in data:
	s = s.split()
	if not s:
		try:
			assert 1920 <= int(cur['byr']) <= 2002
			assert 2010 <= int(cur['iyr']) <= 2020
			assert 2020 <= int(cur['eyr']) <= 2030
			assert 2020 <= int(cur['eyr']) <= 2030
			b = (cur['hgt'][-2:] == 'cm' and 150 <= int(cur['hgt'][:-2]) <= 193)
			b = b or (cur['hgt'][-2:] == 'in' and 59 <= int(cur['hgt'][:-2]) <= 76)
			assert b
			assert re.match("^#[a-f0-9]{6}$", cur['hcl'])
			assert cur['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
			assert re.match("^[0-9]{9}$", cur['pid'])
			ans += 1
		except:
			pass
		cur.clear()
	else:
		for i in s:
			i = i.split(':')
			cur[i[0]] = i[1]

print(ans)