'''
a = 1
b = 2
c = 3
d = 4
a += b
d *= c
c -= a
b *= c
print(a, b, c, d)
'''

'''
X = int(input())
if X % 2 == 0:
	Y = X
if X % 2 == 1:
	Y = X * 2 
print(Y)
'''

# Color cell of chessboard

'''  
x = int(input())        
y = int(input())
if (x + y) % 2 == 1:
   print('white')
else:
   print('black')
'''

'''
x = int(input())
if x == 200:
   print('OK')
elif x == 404:
	print('Not Found')
elif x == 501:
	print('Not implemented')
elif x // 100 == 2:
	print('Success')
elif x // 100 == 5:
	print('Server error')
else:
    print(501)
'''

#print('privet ', 'loh')

'''
a = int(input())
b = int(input())
if a % 7 == 0:
	if b % 3 == 0:
		print(2)
	else:
		print(1)
else:
    print(0)
'''

'''
a = int(input())
if a // 10 == 5:
	if a % 10 != 5:
		print('YES')
	else:
		print('NO')
elif a % 10 == 5:
	if a // 10 != 5:
		print('YES')
	else:
		print('NO')
else:
	print('NO')
'''

'''
X = int(input())
if X == 1 or X == 2 or X == 12:
   print('winter')
elif X == 3 or X == 4 or X == 5:
   print('spring')
elif X == 6 or X == 7 or X == 8:
   print('summer')
elif X == 9 or X == 10 or X == 11:
   print('autumn')
'''

'''
a = int(input())
b = int(input())
c = int(input())
if c == a + b:
	print('+')
elif c == a - b or c == b - a:
	print('-')
else:
    print(':(')
'''

'''
a = int(input())
if a > 100 or a <= 40 and a % 2 == 0:
	print('YES')
else:
	print('NO')
'''

'''
a = int(input()) #nomer
b = int(input()) #data
if a == 1:
	if b % 2 == 0 and b % 7 != 0:
		print('yes')
	else:
		print('no')
elif a == 2:
	if b % 2 == 1 and b % 7 != 0:
		print('yes')
	else:
		print('no')
elif a == 3:
	if b % 3 == 0 and b % 7 != 0:
		print('yes')
	else:
		print('no')
'''

