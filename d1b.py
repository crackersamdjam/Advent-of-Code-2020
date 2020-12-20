import sys
s = list(map(int, sys.stdin.read().strip().split('\n')))
for i in range(len(s)):
    for j in range(i):
        for k in range(j):
            if s[i]+s[j]+s[k] == 2020:
                print(s[i]*s[j]*s[k])

