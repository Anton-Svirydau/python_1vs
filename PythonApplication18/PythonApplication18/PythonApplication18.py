'''
d = dict()
d[50] = 1
d[1000] = 2
d[1000000] = 3
print(d[1000])
'''
'''
countries = dict()  # creating an empty dictionary

countries['Ekaterinburg'] = 'Russia'  # assigning a value by key
countries['Antananarivo'] = 'Madagaskar'
countries['Brest'] = ['France', 'Belarus']  # you can store arrays in a dictionary

print(countries['Brest']) # accessing a value by key

for city in ['Ekaterinburg', 'Antananarivo']:
    print('City ' + city + ' is located in: ' + countries[city])  # access by key using variable
'''
'''
countries = {'Minsk': 'Belarus', 'Almaty': 'Kazakhstan'}

for key, val in countries.items():
    print(key, val)
'''
'''
n = int(input())

marriage_data = {}

for _ in range(n):
    person, spouse = input().split(":")
    marriage_data[person] = spouse
    marriage_data[spouse] = person

m = int(input())

for _ in range(m):
    query = input()
    if query in marriage_data:
        print(marriage_data[query])
    else:
        print("NO_DATA")

'''
'''
from collections import defaultdict

n = int(input())

city_data = defaultdict(list)

for _ in range(n):
    person, city = input().split(":")
    city_data[city].append(person)

sorted_cities = sorted(city_data.keys())

print(len(sorted_cities))

for city in sorted_cities:
    city_data[city].sort()

    print(f"{city} {len(city_data[city])}")

    for resident in city_data[city]:
        print(resident)
'''
'''
from collections import Counter

n = int(input())

bus_routes = [int(input()) for _ in range(n)]

route_counts = Counter(bus_routes)

unique_routes = [route for route, count in route_counts.items() if count == 1]

unique_routes.sort()

print(len(unique_routes))

if unique_routes:
    print(" ".join(map(str, unique_routes)))
'''
'''
from collections import Counter

n = int(input())

bus_routes = [int(input()) for _ in range(n)]

route_counts = Counter(bus_routes)

unique_routes = [route for route, count in route_counts.items() if count == 1]

def first_digit(num):
    return int(str(num)[0])

unique_routes.sort(key=first_digit)

print(len(unique_routes))

if unique_routes:
    print(" ".join(map(str, unique_routes)))
'''
'''
children = {}

mother = 'Thetis'
father = 'Peleus'
child = 'Achilles'

if (mother, father) not in children:
  children[(mother, father)] = []
      
children[(mother, father)].append(child)

print(children)
'''
'''
t = (3, 2, 1)
print(t[0])   
print(t[-1])  

for number in t:
  print(number)
      
print(t[1:2])  
'''
'''
t1 = (1, 2)
t2 = (1, 2)
print(t1 == t2)  

t1 = (1, 2, 3)
t2 = (1, 2)
print(t1 == t2)  

t1 = (1, 2)
t2 = (1, 3)
print(t1 == t2)  

t1 = (1, 2)
t2 = (1, 1)
print(t1 > t2)  

t1 = (1, 2, 3)
t2 = (1, 2)

print(t1 < t2)  
'''

from collections import defaultdict

pixels = defaultdict(list)

def set_pixel(x, y, c):
    pixels[(x, y)].append(c)

def get_pixel(x, y):
    if pixels[(x, y)]:
        return pixels[(x, y)][-1]
    else:
        return "white"

def erase_pixel(x, y):
    if pixels[(x, y)]:
        pixels[(x, y)].pop()

n = int(input())

results = []

for _ in range(n):
    query = input().split()
    if query[0] == 's':
        x, y, color = int(query[1]), int(query[2]), query[3]
        set_pixel(x, y, color)
    
    elif query[0] == 'g':
        x, y = int(query[1]), int(query[2])
        result = get_pixel(x, y)
        results.append(result)
    elif query[0] == 'e':
        x, y = int(query[1]), int(query[2])
        erase_pixel(x, y)

print("\n".join(results))









