'''
print(ord('a'))
print(chr(97))
'''

'''
s = input()
for i in range(len(s)):
	if 64 < ord(s[i]) < 91: 
		s = s[:i] + chr(ord(s[i]) + 32) + s[i+1:] 
print(s)
'''

'''
s = input()
numb = ord(s) - ord('A') + 1
print('s - ' + str(numb))
'''

'''
n = int(input())
s = 0
while n != 0:
	s += n % 10
	n //= 10

print(s)
'''

'''
n = input()
s = 0
for i in range(len(n)):
	s += ord(n[i]) - ord('0')

print(s)
'''

'''
kek = input()
lol = input()
cringe = 0

for i in range(len(kek)):
	if kek.lower()[i] != lol.lower()[i]:
		if kek.lower()[i] < lol.lower()[i]:
			cringe = 1
		break

if cringe == 1:
	print('YES')
else:
	print('NO')
'''

'''
kek = input()
lol = int(input())

print(chr(ord(kek) + lol))
'''

'''
kek = input()
lol = input()

print(abs(ord(kek) - ord(lol)))
'''

'''
kek = input()
lol = ''

for i in range(len(kek)):
	lol += chr(ord(kek[i]) + 1)

print(lol)
'''


