'''
a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] % 7 != 0 and i % 7 != 0:
        a[i] *= -1

print(*a)
'''

'''
a = list(map(int, input().split()))
k = int(input())

for i in range(k):
    e = int(input())
    print(a[e - 1])

print(*list(reversed(a)))
'''

'''
numbers = input().split()

numbers = [int(num) for num in numbers]

total_sum = sum(numbers)

expression = '+'.join(str(num) for num in numbers) + '=' + str(total_sum)

print(expression)
'''
'''
a = list(map(int, input().split()))

print(*a, sep = '+', end = '')
print('=' + str(sum(a)))
'''

'''
a = list(map(int, input().split()))
print(list(reversed(sorted(a)))[4])

a = list(map(int, input().split()))
a = sorted(a)
a.reverse()
print(a[4])

a = list(map(int, input().split()))
a = sorted(a, reverse=True)
print(a[4])
'''

'''
a = list(map(int, input().split()))
a = a[::-1]
print(*a)
'''

'''
a = list(map(int, input().split()))
b = 0

for i in range(1, len(a)):
	if a[i] < a[i-1]:
		b += 1
		
print(b)
'''

'''
a = list(map(int, input().split()))
b = a[0]

for i in range(1, len(a)):
	if a[i] - a[i - 1] > 0:
		b += a[i] - a[i - 1]
		
print(b)
'''

'''
a = list(map(int, input().split()))
b = 0
c = 0

for i in range(2, len(a)):
	if a[i] > a[i-1] + a[i-2]:
		b += 1
		if c < a[i]:
			c = a[i]

if b != 0:
	print(b, c)
else:
	print(0, 0)
'''

'''
a = list(map(int, input().split()))
s = 0
for i in a:
	s += i
print(s)
'''

'''
for i in "AEIUO":
	print(i)
'''

'''
a = list(map(int, input().split()))
cnt = 0
for i in a:
	if i in [5, 10, 13]:
		cnt += 1
print(cnt)
'''

'''
lol = [3, 7, 12, 29, 50, 51, 53, 75]
cringe = int(input())
kek = 0

for i in lol:
	if cringe % i == 0:
		kek = 1
		print('YES')
		break

if kek == 0:
	print('NO')
'''

'''
cringe = input()
kek = 0

for i in cringe:
	if i in 'AEIOUaeiou':
		kek += 1

print(kek)
'''

'''
text = input().split()
kek = 0
cringe = ['code', 'problem', 'solution', 'ok', 'wa']

for i in text:
	if i.lower() in cringe:
		kek += 1

print(kek)
'''

'''
L=[100,200,300]
print(L.pop())
'''

'''
n = int(input())
a = [] 

for i in range(n):
	s = int(input())
	a.append(s)

a = a[::-1]
print(*a)
'''

'''
kek = list(map(int, input().split()))
lol = list(map(int, input().split()))
lul = list(map(int, input().split()))

for i in range(len(lul)):
	if i in lol:
		lol.pop(lol.index(i))

print(lol)
'''

kekw = [1 2 3]
print(kekw)










