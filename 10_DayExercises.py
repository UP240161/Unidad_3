import sys
sys.path.append(r'c:\Users\ESTUDIANTE\Downloads\Unidad_3')  # Adjust the path to where day_exercise.py is located
from _DayExercises import 

# Ahora puedes usar la lista de países
for country in countries:
    if "land" in country:
        print(country)
# Level 1
#Exercise 1
for i in range(0, 11):
    print(i)

k = 0
while k <= 10:
    print(k)
    k += 1

#Exercise 2
for i in range(10, -1, -1):
    print(i)

k = 10
while k >= 0:
    print(k)
    k -= 1

#Exercise 3
hash_string = '#'
for i in range(1, 8):
    print(hash_string * i)

#Exercise 4
for i in range(1, 9):
    for j in range(1, 9):
        print("#", end=' ')
    print()

#Exercise 5
for i in range(0, 11):
    print(i, "x", i, "=", i * i)

#Exercise 6
for lang in ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']:
    print(lang)

#Exercise 7
for i in range(0, 101):
    if i % 2 == 0:
        print(i)

#Exercise 8
for i in range(0, 101):
    if i % 2 != 0:
        print(i)

# Level 2
#Exercise 1
sum_nums = 0
for i in range(0, 101):
    sum_nums += i
print("The sum of all numbers is", sum_nums)

#Exercise 2
even_sum = 0
odd_sum = 0
for i in range(0, 101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("The sum of all even numbers is", even_sum)
print("The sum of all odd numbers is", odd_sum)
#Level 3
#Exercise 1
list_c = countries["country_list"]
for country in list_c:
    if "land" in country:
        print(country)

#Exercise 2
fruity_list = ['banana', 'orange', 'mango', 'lemon']
rev = []
for i in range(3, -1, -1):
    rev.append(fruity_list[i])
print(rev)

#Exercise 3
# noinspection DuplicatedCode
list_data = countries_data.data
total_languages_initial = []
for i in list_data:
    total_languages_initial.extend(i["languages"])
print("Languages = ", len(set(total_languages_initial)))
counts = {}
for i in total_languages_initial:
    counts[i] = counts.get(i, 0) + 1


def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


counts = sort_dict_by_value(counts, True)
for i in list(counts.items())[:10]:
    print(i)
populations = {}
for i in list_data:
    populations[i["name"]] = i["population"]
populations = sort_dict_by_value(populations, True)
for i in list(populations.items())[:10]:
    print(i)