import re, sys
data = sys.stdin.read().split('\n')
ans = 0
st = set()

for s in data:
	v = 0
	if not s:
		ans += 26-len(st);
		st.clear()
	else:
		for c in range(ord('a'), ord('z')+1):
			if chr(c) not in s:
				st.add(c)

print(ans)