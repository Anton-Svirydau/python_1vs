'''
cringe = [1, 2, 3, 4, 5]
b = [2, 4, 6]

for i in range(len(b)):
    if b[i] in cringe:
        cringe.pop(cringe.index(b[i]))
    else:
        cringe.append(b[i])

print(*cringe)
'''

'''
cringe = list(map(int, input().split()))
kek = list(map(int, input().split()))
lol = list(map(int, input().split()))

for i in range(len(lol)):
    if lol[i] in kek:
        kek.pop(kek.index(lol[i]))
    else:
        kek.append(lol[i])

print(*kek)
'''

'''
print(list('abcd'))
print(''.join(list('abcd')))
'''

'''
s = input()
s = list(s)
cringe = []

for i in range(len(s) - 1):
    cringe.append("^_^")
    cringe.append(s[i + 1])

cringe.insert(0, s[0])
print(''.join(cringe))
'''

'''
cringe_original = list(map(int, input().split()))
lol = int(input())

for i in range(lol):
    cringe_NoNoriginal = cringe_original.copy()
    kek = int(input())
    for i in range(len(cringe_NoNoriginal)):
        cringe_NoNoriginal[i] = cringe_NoNoriginal[i] - (cringe_NoNoriginal[i] // kek)
    print(*cringe_NoNoriginal)
'''

'''
cringe_original = list(map(int, input().split()))
lol = int(input())

for i in range(lol):
    cringe_NoNoriginal = cringe_original.copy()
    kek = int(input())
    cringe_NoNoriginal.append(kek)
    cringe_NoNoriginal = sorted(cringe_NoNoriginal)
    cringe_NoNoriginal = cringe_NoNoriginal[::-1]
    print(*cringe_NoNoriginal)
'''

'''
def replace_character(s, index, new_char):
    if index < 0 or index >= len(s):
        print()
        return s
    s_list = list(s)
    s_list[index] = new_char
    return ''.join(s_list)

s = input()
q = int(input())

for i in range(q):
    index, new_char = input().split()
    index = int(index) - 1
    s = replace_character(s, index, new_char)

print(s)
'''

'''
cringe_string = input()
lol = int(input())
c = list(cringe_string)


for i in range(lol):
    cringe_zamena = list(input().split())
    b = int(cringe_zamena[0]) - 1
    c[b] = cringe_zamena[1]

print(''.join(c))
'''

'''
a = list(map(int, input().split()))
q = list(map(int, input().split())) 
for x in q:
	print(a.count(x))
'''

'''
a = list(map(int, input().split()))
k = int(input())
for _ in range(k):
	t, x = map(int, input().split())
	if t == 1:
		for i in range(len(a)):
			if a[i] % x == 0:
				a[i] += 1
	else:
		s = 0
		for i in range(len(a)):
			if a[i] % x == 0:
				s += a[i]
		print(s)
'''

'''
a = list(map(int, input().split()))
k = int(input())
for _ in range(k):
	l, r = map(int, input().split())
	l -= 1
	r -= 1 
	s = 0
	for i in range(l, r + 1): 
		s += a[i] * a[i]
	print(s)
'''

'''
a = list(map(int, input().split()))
k = int(input())
for _ in range(k):
	l, r = map(int, input().split())
	l -= 1
	r -= 1 
	b = a[l:r+1]
	s = 0
	for i in b:
		s += i * i
	print(s)
'''

'''
n = int(input())
a = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    s = 0
    for i in range(l, r - 1):
        if a[i - 1] < a[i] > a[i + 1]:
            s += 1
    print(s)
'''

'''
n = int(input())
a = list(map(int, input().split()))
for i in range(len(a)):
    cnt = 0
    for j in range(i + 1, len(a)):
        if a[i] > a[j] and j != n - 1:
            cnt += 1
        if a[i] <= a[j]: 
            break
    if i != n - 1:
        cnt += 1
    print(cnt)
'''

'''
n = int(input())
a = list(map(int(), input().split()))
for i in range(n):
    cnt = 0
    for j in range(i + 1, n):
        if i == n - 1:
            cnt = 0
            break
        if a[i] > a[j]:
            cnt += 1
        else:
            cnt += 1
            break
    print(cnt)
'''

'''
a = list(map(int, input().split()))
s = 0
for i in a:
	s += i
	print(s)
'''
'''
k = int(input())
a = int(input())
n = list(map(int, input().split()))
s = 0
for i in n:
    if i % k == 0:
        s += 1
    print(s)
'''

'''
a = 0
b = 0
while a != -1:
    a = int(input())
    if b < a:
        b = a
    if a != -1:
        print(b)
'''

'''
a = list(map(int, input().split()))
c = [0, 0, 0, 0, 0]
for i in a:
	if 1 <= i <= 5:
		c[i-1] += 1 
print(*c)
'''

'''
a = [1, 2] + [3, 4]
b = [1] * 3 + [2] * 4
print(*a)
print(*b)
'''

'''
a = list(map(int, input().split()))
ok = [ a[0] ] 
cnt = 0
for i in range(1, len(a)):
	if ok[-1] < a[i]:
		cnt += 1
	else:
		ok.append(a[i])
print(cnt)
'''

'''
l, r = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
b = []
c = [0] * (r - l + 1)
for i in a:
    if l <= i <= r:
        b.append(i)
b.sort()
cnt = 0
for k in range(len(c)):
    c[k] += 1
    cnt += 1
    for m in range(cnt, len(b)):
        if b[m] == b[m-1]:
            cnt += 1
            c[k] += 1
        else:
            break
d = [b[0]]
for l in range(1, len(b)):
    if b[l] != b[l-1]:
        d.append(b[l])
for p in range(len(d)):
    print(d[p], ': ', c[p], sep = '')
'''

'''
l, r = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
b = []
c = [0] * (r - l + 1)
for i in a:
    if l <= i <= r:
        b.append(i)
b.sort()
cnt = 0
for k in range(len(c)):
    c[k] += 1
    cnt += 1
    for m in range(cnt, len(b)):
        if b[m] == b[m-1]:
            cnt += 1
            c[k] += 1
        else:
            break
d = [b[0]]
for l in range(1, len(b)):
    if b[l] != b[l-1]:
        d.append(b[l])
if d.count(r) == 0:
    d = d + [r]
    c[len(d)-1] = 0
for p in range(len(d)):
    print(d[p], ': ', c[p], sep = '')
'''

'''
l, r = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
b = [l]
k = 0
while b[len(b) - 1] != r:
    b.append(b[len(b) - 1] + 1)
for i in range(len(b)):
    k = a.count(b[i])
    print(b[i], ': ',k , sep = '')
'''













