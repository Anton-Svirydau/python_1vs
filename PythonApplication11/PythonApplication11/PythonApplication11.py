'''
list_1 = input().split()
print(len(list_1))
'''

'''
list_1 = input().split()
cringe = 0

for i in range(len(list_1)):
	if list_1[i] == 'I':
		cringe += 1
		
print(cringe)
'''

'''
list_1 = input().split()
cringe = 0

for i in range(len(list_1)):
	if list_1[i] == 'I':
		cringe = i + 1
		break
	else:
		cringe = -1
		
print(cringe)
'''

'''
list_1 = input().split()
cringe = 0

for i in range(len(list_1)):
	if list_1[i].isupper():
		cringe += 1
		
print(cringe)
'''

'''
cringe = list(map(int, input().split()))
print(sum(cringe))
print(max(cringe) - min(cringe))
'''

'''
list_1 = list(map(int, input().split()))
cringe = 0

for i in range(len(list_1)):
	if list_1[i] % 7 == 0:
		cringe += 1
		
print(cringe)
'''

'''
a, b = map(int, input().split())
print(a + b)
'''

'''
a, b, A, B = map(int, input().split())
c = a
d = b
cringe = 0

while True:
	if A >= a:
		a += c
		cringe += 1
	else:
		break
		
while True:
	if B >= b:
		b += d
		cringe += 1
	else:
		break
		
print(cringe)
'''

'''
a, b, c = map(int, input().split())
print(a + b + c - min(a, b, c))
'''

'''
a = list(map(int,input().split()))
print(a)
print(*a)
print(*a, sep='+')
'''

#sum
'''
a = list(map(int, input().split()))
s = 0
for i in range(len(a)):
	s += a[i]
print(s)
'''

#max
'''
a = list(map(int, input().split()))
best = 0
for i in range(1, len(a)):
	if a[i] > a[best]:
		best = i
print(a[best])
'''

#min
'''
a = list(map(int, input().split()))
best = 0
for i in range(len(a)):
	if a[i] < a[best]:
		best = i
print(a[best])
'''

'''
list_1 = list(map(int, input().split()))
cringe = 0

for i in range(len(list_1)):
	if list_1[i] % 7 == 0:
		cringe += list_1[i]

print(cringe)
'''

'''
list_1 = list(map(int, input().split()))
cringe = 0

for i in range(len(list_1)):
	cringe += list_1[i] % 3

print(cringe)
'''

'''
a = list(map(int, input().split()))
best = 0
for i in range(len(a)):
	if a[i] > a[best]:
		best = i
print(best + 1)
'''

'''
a = list(map(int, input().split()))
best = 0

for i in range(len(a)):
	if a[i] <= abs(min(a)):
		best += a[i]

print(best)
'''

'''
a = list(map(int, input().split()))
best = 0
cringe = 0

for i in range(len(a)):
	if a[i] % 2 != 0:
		best = i
		cringe = 1
		break

if cringe == 1:
	for i in range(len(a)):
		if a[i] % 2 != 0 and a[i] < a[best]:
			best = i
	print(a[best])
else:
	print(-1)
'''

'''
a = list(map(int, input().split()))
best = 0

for i in range(len(a)):
	if a[i] < 0:
		best = a[i]
		break

if best != 0:
	for i in range(len(a)):
		if a[i] > best and a[i] < 0:
			best = a[i]
	print(best)
else:
	print(-1)
'''

'''
a = list(map(int, input().split()))
cringe = min(a)

for i in range(len(a)):
	a[i] -= cringe

print(*a)
'''


a = list(map(int, input().split()))

for i in range(len(a)):
	if a[i] % 7 != 0:
		a[i] = -a[i]
	if a[i] % 7 == 0 and (i + 1) % 7 == 0 and i != 0:
		a[i] = -a[i]

if a[0] == -55:
	a[0] == 55

print(*a)





