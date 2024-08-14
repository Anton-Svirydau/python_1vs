'''
def find_numbers(c):
    for a in range(1, c):
        b_squared = c**2 - a**2
        b = int(b_squared**0.5)
        if a**2 + b**2 == c**2:
            return "YES"
    return "NO"

# data input
c = int(input())

# output result
result = find_numbers(c)
print(result)
'''
#==
'''
favorite_number = int(input())
cringe = 0

for a in range(1, favorite_number):
    b_squared = favorite_number**2 - a**2
    b = int(b_squared**0.5)
    if a**2 + b**2 == favorite_number**2:
        cringe += 1
        break

if cringe != 0:
    print('YES')
else:
    print('NO')
'''

'''
string_1 = input()
big_1 = 0
small_1 = 0

for i in range(len(string_1)):
    if string_1[i].isupper():
        big_1 += 1
    if string_1[i].islower():
        small_1 += 1

if big_1 > small_1:
    print('BIG')
elif big_1 == small_1:
    print('SAME')
else:
    print('SMALL')
'''

'''
favorite_number = int(input())

for i in range(1, 20):
    flag = False
    for j in range(1, 20):
        if i ** 2 + j ** 2 == favorite_number ** 2:
            flag = True
            print('YES')
            break
        elif i == favorite_number and j == favorite_number:
            print('NO')
    if flag:
        break
'''

'''
s = input()
symb = 'A' 
appears = False

for i in range(len(s)):
	if s[i] == symb:
		appears = True

if appears:
	print('yes')
else:
	print('no')
'''

#You're interested in reading other people's code, aren't you?

'''
string_2 = input() 
flag = False

for i in range(1,len(string_2)):
	if string_2[i].isupper():
		flag = True

if flag:
	print('YES')
else:
	print('NO')
'''