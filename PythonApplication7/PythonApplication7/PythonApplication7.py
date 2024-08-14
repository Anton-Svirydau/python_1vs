'''
a = 2 + 2 == 5
print(a)
'''

'''
a = True
if a:
	a = False
if not a:
	print(not a)
'''

'''
s = input()

if s.isupper():
	print('YES')
else:
	print('NO')
'''

'''
N = int(input()) 
M = int(input())
x = 0
y = 0
z = 0

for i in range(N):
	A = int(input())
	if A > M:
		x += 1
	if A % 2 == 0:
		y += 1

if x != 0:
	print('YES')
else:
	print('NO')

if y != 0:
	print('YES')
else:
	print('NO')
'''

'''
def check_conditions(sequence, M):
    condition_1 = any(num > M for num in sequence)
    condition_2 = any(num % 2 == 0 for num in sequence)
    condition_3 = any(a < b < c for a, b, c in zip(sequence, sequence[1:], sequence[2:]))

    return condition_1, condition_2, condition_3

N, M = map(int, input().split())
sequence = [int(input()) for _ in range(N)]

result = check_conditions(sequence, M)

for res in result:
    print("YES" if res else "NO")
'''

'''
mark = input()

if mark.isdigit():
	print('YES')
elif mark.startswith('result: ') and (mark[8:].islower() or mark[8:].isdigit()):
	print('YES')
else:
	print('NO')
'''





