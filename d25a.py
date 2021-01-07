# diffie hellman key exchange
import sys
data = sys.stdin.read().strip().split('\n')

mod = 20201227
pa = int(data[0])
pb = int(data[1])

a = 0
v = 1
while v != pa:
	v = v*7%mod
	a += 1

k = 1
for _ in range(a):
	k = k*pb%mod

print(k)