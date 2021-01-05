import sys
boxes = sys.stdin.read().strip().split('\n')

def rot(a):
	b = []
	for i in range(len(a)):
		b.append('')
		for j in range(len(a)):
			b[i] += a[-j-1][i]
	return b

def flip(a):
	return a[::-1]

pat = [
'                  # ',
'#    ##    ##    ###',
' #  #  #  #  #  #   ']
h = len(pat)
w = len(pat[0])
sz = len(boxes)

def go():
	for i in range(sz-h+1):
		for j in range(sz-w+1):
			ok = 1
			for k in range(h):
				for l in range(w):
					if pat[k][l] == '#' and boxes[i+k][j+l] == '.':
						ok = 0

			if not ok:
				continue

			for k in range(h):
				for l in range(w):
					if pat[k][l] == '#':
						# boxes[i+k][j+l] = '$'
						t = list(boxes[i+k])
						t[j+l] = '$'
						boxes[i+k] = ''.join(t)

for __ in range(2):
	for _ in range(4):
		go()
		boxes = rot(boxes)
	boxes = flip(boxes)

cnt = 0
for i in boxes:
	cnt += i.count('#')
print(cnt)