'''
size = int(input())

game_map = []
for row_idx in range(size):
  next_row = input()
  game_map.append(next_row)

total_cost = 0
for row in game_map:
  for block in row:
    if block == '#':
      total_cost += 1000
    else:
      total_cost += 100

print(total_cost)
'''

'''
string_1 = input().split()
list_1 = []
upper_1 = 0
vowels_1 = 0
cnt = 0
for words in string_1:
    upper_1 = 0
    vowels_1 = 0
    for letters in words:
        if 65 <= ord(letters) <= 90:
            upper_1 += 1
        if ord(letters) == 65 or ord(letters) == 69 or ord(letters) == 73 or ord(letters) == 79 or ord(letters) == 85 or ord(letters) == 89 or ord(letters) == 97 or ord(letters) == 101 or ord(letters) == 105 or ord(letters) == 111 or ord(letters) == 117 or ord(letters) == 121:
            vowels_1 += 1
    if upper_1 > vowels_1:
        cnt += 1
print(cnt)
'''

'''
floor, apartment = map(int, input().split())

building = []
for floor_1 in range(floor):
    apartment_1 = input()
    building.append(apartment_1)

cnt = 0
for floor_2 in building:
    for apartment_2 in range(1, apartment):
        if floor_2[apartment_2 - 1] == '1' and floor_2[apartment_2] == '1':
            cnt += 1
            break
print(cnt)
'''

'''
size = int(input())
cringe = [0] * size

cake = []
for row_idx in range(size):
  next_row = input()
  cake.append(next_row)

for row_1 in cake:
    for k in range(len(row_1)):
        if row_1[k] == 'C':
            cringe[k] += 1

cnt_1 = 0
for i in cringe:
    if i == 0:
        print('NO')
        cnt_1 += 1
        break
if cnt_1 == 0:
    print('YES')
'''

'''
student_amount = int(input())

names = []
grades = []
for student_idx in range(student_amount):
  name, grade = input().split()
  names.append(name)
  grades.append(int(grade))

for student_i in range(student_amount):
  for student_j in range(student_amount):
    if grades[student_i] > grades[student_j]:
      grades[student_i], grades[student_j] = grades[student_j], grades[student_i]
      names[student_i], names[student_j] = names[student_j], names[student_i]

for student_idx in range(student_amount):
  print(names[student_idx], grades[student_idx])
'''

'''
student_amount = int(input())

students = []
for student_idx in range(student_amount):
  name, grade1, grade2, grade3, grade4 = input().split()
  students.append([name, int(grade1), int(grade2), int(grade3), int(grade4)])

for student_i in range(student_amount):
  for student_j in range(student_amount):
    data_i = students[student_i]
    data_j = students[student_j]
    grades_i = data_i[1] + data_i[2] + data_i[3] + data_i[4]
    grades_j = data_j[1] + data_j[2] + data_j[3] + data_j[4]
    if grades_i > grades_j:
      students[student_i], students[student_j] = students[student_j], students[student_i]

for student in students:
  print(student[0], student[1], student[2], student[3], student[4])
'''

'''
original = [1, 2, 4, 6]
modified = [element * 2 for element in original]
print(original, modified)
'''

'''
last_digits = [number for number in range(1, 101) if number % 5 == 0]
print(last_digits)
'''

'''
zeroes = [0 for _i in range(30)]
print(zeroes)
'''

'''
zeroes10x10 = [
  [0 for _j in range(7)]
  for _i in range(5)
]
print(zeroes10x10)
'''

'''
def double(x):
  return x * 2

print(double(5))  
print(double(0))  
'''

'''
def add(a, b):
  return a + b
print(add(5, 10))
'''

'''
def answer_to_life_the_universe_and_everything():
  return 42
print(answer_to_life_the_universe_and_everything())
'''

'''
def no_returns():
  for i in range(5):
    print(i * 2)

print(no_returns())  # None
'''

'''
name = 'Maksim'

def hello(name):
  print('Hi,', name)

def goodbye(name):
  print('Bye,', name)

def i_say():
  print(name, 'tell:')

i_say() 
hello('Nastya')  
goodbye('Lev')  
'''
'''
def minmax(a, b):
  if a < b:
    return a, b
  return b, a

lesser, greater = minmax(1, 42)
print(lesser)  # 1
print(minmax(1, 42))  # (1, 42)
'''
'''
def sumnum(x):
    a = 0
    while x >= 9:
        a += x % 10
        x = x // 10
    a += x
    return a

sum = 0
sumnum_list = list(map(int, input().split()))
for i in sumnum_list:
    if i % 2 == 1:
        sum += sumnum(i)
print(sum)
'''

'''
n = int(input())

def index_true(x):
    a = 0
    if 1 <= x <= n:
        a = 1
    return a

true_moves = 0
Kolya_moves = list(map(int, input().split()))
Kolya_moves_new = []

for e in Kolya_moves:
    if e not in Kolya_moves_new:
        Kolya_moves_new.append(e)

for i in Kolya_moves_new:
    true_moves += index_true(i)

print(true_moves)
'''
'''
interest_rate = 1.01

initial_debt = 1000

def calculate_debt(days):
  if days < 0:
    print('cringe :(')
    return 0  

  if days == 0:
    return initial_debt

  debt_yesterday = calculate_debt(days - 1)  
  return debt_yesterday * interest_rate

print('+/-', int(calculate_debt(365)), '$')  
'''
'''
def reverse_sequence():
    num = int(input())
    if num != -1:
        reverse_sequence()
        print(num)

reverse_sequence()
'''
'''
set_of_numbers = set(map(int, input().split()))
print(len(set_of_numbers))
'''
'''
set_1 = {4, 230, "Hello", True}  
set_2 = {4, 320, "Hi", False, True} 

print("+: ", set_1 | set_2)
print("+: ", set_1 & set_2)
print("- 1 and 2: ", set_1 - set_2)
print("- 2 and 1: ", set_2 - set_1)
'''
'''
set_of_numbers_1 = set(map(int, input().split()))
set_of_numbers_2 = set(map(int, input().split()))
set_of_numbers_3 = set_of_numbers_2 & set_of_numbers_1
print(len(set_of_numbers_3))
'''
'''
list_1 = list(map(int, input().split()))
set_of_numbers_1 = set(list_1)
cringe = 0

for i in set_of_numbers_1:
    if list_1.count(i) % 2 == 1:
        cringe += 1

print(cringe)
'''
'''
def count_odd_occurrences(numbers):
    count_dict = {}
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    
    odd_count = sum(1 for count in count_dict.values() if count % 2 != 0)
    return odd_count

numbers = list(map(int, input().strip().split()))

result = count_odd_occurrences(numbers)
print(result)
'''
'''
def count_odd_occurrences_in_both(arr1, arr2):
    def count_occurrences(arr):
        count_dict = {}
        for num in arr:
            count_dict[num] = count_dict.get(num, 0) + 1
        return count_dict

    count1 = count_occurrences(arr1)
    count2 = count_occurrences(arr2)

    common_odd_count = 0
    all_numbers = set(count1.keys()).union(set(count2.keys()))

    for num in all_numbers:
        count_in_arr1 = count1.get(num, 0)
        count_in_arr2 = count2.get(num, 0)
        if count_in_arr1 > 0 and count_in_arr2 > 0:
            if count_in_arr1 % 2 != 0 or count_in_arr2 % 2 != 0:
                common_odd_count += 1

    return common_odd_count

arr1 = list(map(int, input().strip().split()))
arr2 = list(map(int, input().strip().split()))

result = count_odd_occurrences_in_both(arr1, arr2)
print(result)

'''
'''
d = dict()
d[50] = 1
d[1000] = 2
d[1000000] = 3
print(d[1000000], d[50], d[1000])
'''
'''
d1 = dict()  
d2 = {} 
d3 = {'A': 1, 'B': 2, 4: 'D'}  
print(d3['A'])
'''





















