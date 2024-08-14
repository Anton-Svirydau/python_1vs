'''
answer = input()

while answer != 'anime':
    answer = input()

print('chel, ti...')
'''

'''
cringe = 0
wtf = int(input())

while wtf > 0:
	cringe += wtf
	wtf = int(input())
	
print(cringe)
'''

'''
cringe = 1
wtf = input()

while wtf.isalpha():
	cringe += 1
	wtf = input()

print(cringe)
'''

'''
cringe = 0
kek = int(input())
lol = int(input())

while kek < lol:
	kek *= 2
	cringe += 1

print(cringe)
'''

'''
cringe = 0
kek = int(input())
lol = int(input())

while kek >= lol:
	kek *= 2
	lol *= 3
	cringe += 1

print(cringe)
'''

'''
cringe = 0
kek = int(input())
wtf = int(input())
lol = int(input())

while kek < lol:
	kek += (kek % wtf) + 1
	cringe += 1

print(cringe)
'''

'''
number = int(input())
given_number = number
digits = 0

while number > 0:
  digits += 1
  number //= 10

print('In', given_number, '-', digits, 'numbers')
'''

'''
number = int(input())
given_number = number
even_digits = 0  
odd_digits = 0  

while number > 0:
  last_digit = number % 10
  if last_digit % 2 == 0:
    even_digits += 1
  else:
    odd_digits += 1
  number //= 10

print('In', given_number, '-', even_digits,
      'even and', odd_digits, 'odd numbers')
'''

'''
kek = int(input())
cringe = 0

while kek % 9 != 0:
	kek *= 10
	kek += 1
	cringe += 1

print(cringe)
'''

'''
cringe = 0
kek = int(input())
lol = int(input())

while kek < lol:
	if kek < 1000:
		kek += 2
	else: 
		kek += kek // 500
	cringe += 1

print(cringe)
'''

'''
cringe = 0
wtf = 1991
kek = int(input())
lol = int(input())

while kek < lol:
	if wtf % 2 == 1:
		kek += kek % 11
	else:
		kek += 5
	cringe += 1
	wtf += 1

print(cringe)
'''

'''
cringe = input()

while True:
	if cringe[0] == 'A':
		break
	elif cringe[0] != 'A' and len(cringe) == 1:
		cringe = ''
		break
	else:
		cringe = cringe[1:]

print(cringe)
'''

'''
cringe = 0
kek = 0
lol = 1

while True:
	if kek > 32 or lol == 0:
		break
	else:
		lol = int(input())
		kek += lol
		cringe += 1

print(cringe)
'''

'''
cringe = 0
kek = 0

while True:
	if kek > 21:
		cringe -= 1
		break
	else:
		lol = input()
		if lol == '2':
			kek += 2
		elif lol == '3':
			kek += 3
		elif lol == '4':
			kek += 4
		elif lol == '5':
			kek += 5
		elif lol == '6':
			kek += 6
		elif lol == '7':
			kek += 7
		elif lol == '8':
			kek += 8
		elif lol == '9':
			kek += 9
		elif lol == '10':
			kek += 10
		elif lol == 'J':
			kek += 10
		elif lol == 'Q':
			kek += 10
		elif lol == 'K':
			kek += 10
		elif lol == 'A':
			kek += 11
		cringe += 1

print(cringe)
'''

'''
def HelloWorld(str):
	print(str)

HelloWorld('print')
'''


