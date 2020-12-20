import sys
s = list(map(int, sys.stdin.read().strip().split('\n')))
for i in range(len(s)):
    for j in range(i):
        if s[i] + s[j] == 2020:
            print(s[i]*s[j])

