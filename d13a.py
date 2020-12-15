import sys, math
t = int(input())
a = input().split(',')
ans = [10**9, 0]

for i in a:
	if i != 'x':
		i = int(i)
		ans = min(ans, [(t-1)//i*i+i-t, i])

print(ans[0]*ans[1])