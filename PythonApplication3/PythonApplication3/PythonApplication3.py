'''
for i in range(11):
  for j in range(11):
    print(i, j, i + j)
    '''

'''
for i in range(4):
  for j in range(4):
    for k in range(4):
      print(i, j, k, i + j + k)
      '''

'''
for i in range(3):
  for j in range(3):
    for k in range(3):
      for l in range(3):
        print(i, j, k, l, i + j + k + l)
'''

'''
for i in range(1, 11):
  for j in range(1, 11):
    if i + j == 15:
      print(i, j)
'''

'''
n = int(input())

for i in range(n + 1):
  print(i)  

  for j in range(i + 1): 
    if j % 2 == 1:
      print(j)

  print('==========') 
'''

'''
a = int(input())
b = int(input())
s = input()

for i in range(a):
    for j in range(b):
        if j != b - 1:
            print(s, end = '')
        else:
            print(s)
'''

'''
n = int(input())
s = input()

for i in range(n):
    for j in range(n):
        if i == j:
            print(s)
        elif i > j:
            print(s, end = '')
'''

'''
a = int(input())
b = int(input())

for i in range(a, b + 1):
  for j in range(a * 2, b * 2 + 1):
    print(i, j)
'''

'''
s = int(input())

for i in range(101):
  print('number', i, '?') 

  if s == i:  
    print('number:', i)  
    break  
  else: 
    print('go ahead')
'''

'''
a = int(input())
b = int(input())

for i in range(1, 101):
    if i % a == 0 and i % b == 0:
        print(i)
        break
'''

'''
n = int(input())

for i in range(n):
    a = int(input())
    if a % 2 == 1:
        p = 1
        for j in range(1, a):
            p *= j
        print(p)
        continue

    print(a)
'''














