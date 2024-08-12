import math

'''
a = input()

print(a[3], a[1], sep = '')
'''

'''
s = "Sunday"
k = int(input())

print(s[k - 1])
'''

'''
s = input()
n = int(input()) 

for i in range(n):
	ndx = int(input())
	ndx -= 1 
	print(s[ndx])
'''

'''
s = 'Sunday'
n = int(input())

for i in range(n):
	k = int(input())
	print(s[-k])
'''

'''
n = int(input())
a = 0 

for i in range(n):
	s = input()
	if s[0] == s[-1]:
		a += 1

print(a)
'''

'''
s = input()

if s.count('!') >= 1:
	print(s.upper())
else:
	print(s.lower())
'''

'''
s = input()
r = int(input())

if s.count('s', 0, r) % 2 == 1:
	print('yes')
else:
	print('no')
'''

'''
s = input()
l = int(input())
r = int(input())

if s.find('F', l, len(s) - r) != -1:
	print('YES')
else:
	print('NO')
'''

'''
s = input()
n = 0

for i in range(len(s)):
	if i % 2 == 0 and s[i] == 'T':
		n += 1

print(n)
'''

'''
a = input()
b = input()
n = 0

for i in range(len(a)):
	if a[i] == b[i]:
		n += 1

print(n)
'''

'''
s = input()
t = input()

for i in range(len(s)):
	if s[i] >= t:
		n = i + 1
		break

print(n)
'''

'''
s = input()
t = input()
a = 'cringe'

for i in range(len(s) - 1, -1, -1):
	if s[i] <= t:
		a = s[i]
		print(a)
		break

if a == 'cringe':
	print(-1)
'''

'''
s = 'ABCDEF'
print(s[1:1000])
print(s[5:3])
print(s[3:3])
print(s[-1000:-1])
'''

'''
s = 'ABCDEF'
print(s[2:])
print(s[:4])
'''

'''
s = 'Tachka'
s = s[:1] + "o" + s[2:]
print(s)
'''

'''
s = 'Cringe'
print(s[5:3:-1])
'''

'''
s = 'abcde'
print(s[len(s):0:-1] + s[0])
'''

'''
s = input()
l = int(input())
d = int(input())

print(s[(l - 1):(l + d - 1)])
'''

'''
s = input()
k = int(input())
t = input()

s = s[0:k - 1] + t + s[k:len(s)]
print(s)
'''