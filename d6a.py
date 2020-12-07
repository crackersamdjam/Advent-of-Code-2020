import re, sys
data = sys.stdin.read().split('\n')
ans = 0
st = set()

for s in data:
	v = 0
	if not s:
		ans += len(st);
		st.clear()
	else:
		for c in s:
			st.add(c)

print(ans)