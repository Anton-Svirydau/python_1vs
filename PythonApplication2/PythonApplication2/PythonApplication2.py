'''
for i in range(101):
  print(i)
'''

'''
for i in range(10, 21):
  print(i)
'''

'''
n = 0

for i in range(11):
  n += i

print(n)
'''

'''
print('Write number slagaemih')   

n = int(input())
s = 0

for i in range(n):
    a = int(input())
    s += a

print(s)
'''

'''
n = int(input("n: "))
s = 0

result_string = ""

for i in range(1, n + 1):
    s += i
    result_string += str(i)
    if i < n:
        result_string += "+"

print(f"{result_string}={s}")
'''

'''
N = int(input())
p = 1

for i in range(1, N + 1):
    p *= i

print(p)
'''

'''
n = int(input()) 
s = 0

for i in range(1, n + 1):
    s += i
    if i != n:
        print(i, end='+')

print(n,end='=')
print(s)
'''

'''
print('python', end=' ')
print('my', end=' ')
print('favorite', 'opp', sep=' - ')
'''

'''
ans = 0
for i in range(3, 7):
	if i % 2 == 0:
		print('+', i, sep='', end='')
		ans += i
	else:
		print('-', i, sep='', end='')
		ans -= i
print('=', ans, sep='')
'''

'''
N = int(input())
K = int(input())
p = 0
A = 0

for i in range(1, N + 1):
    A = int(input())
    p += K * A

print(p)
'''

'''
N = int(input())
Q = int(input())
s = 0

for i in range(1, N + 1):
    s += Q + i - 1

print(s)
'''

'''
M = int(input())
N = int(input())
s = 0
ss = 0


for i in range(1, N + 1):
    A = int(input())
    s += A // M
    ss += A % M

print(s)
print(ss)
'''

'''
a = int(input())
n = int(input())

for i in range(1, n + 1):
    c = int(input())
    a *= 2
    a -= c
    if a < 0:
        a = 0

print(a)
'''

'''
A = int(input())
B = int(input())

for i in range(A, B + 1):
    if i % 5 == 0:
        print(i, end=' ')
        '''

'''
n = int(input())  

for i in range(n):  
  number = int(input())  

  if number % 3 == 0:  
    print(number)
  elif (number - 1) % 3 == 0:  
    print(number - 1)
  else: 
    print(number + 1)
    '''

'''
N = int(input())
s = 0

for i in range(1, N + 1):
    A = int(input())
    if i > 1 and A > s:
        print('YES')
    elif i > 1 and A <= s:
        print('NO')
    s = A
'''

'''
for i in range(0, 11, 2):
  print(i)
'''

'''
for i in range(10, -1, -1):
  print(i, end = ' ')
'''



