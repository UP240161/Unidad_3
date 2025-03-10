#Exercise 1
Lst=()

#Exercise 2
Lst=(1, 2, 3, 4, 5, 6)

#Exercisse 3

longitud = len(Lst)

#Exercise 4

first_item = Lst[0]
middle_item = Lst[len(Lst) // 2]
last_item = Lst[-1]

#Exercise 5
Name= 'Diego Garduño González'
Age= 18
Height= 1.75
Matrial_status= 'Single'
Adress= 'Morelos II Carlos M. Bustamante 326'
Mixed_Data_Types = (Name, Age, Height, Matrial_status, Adress)

#Exercise 6 

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

#Exercise 7

print(len(it_companies))

#Exercise 8

print(it_companies[0], it_companies[3], it_companies[6])

#Exercise 9

print("First item:", first_item)
print("Middle item:", middle_item)
print("Last item:", last_item)

#Exercise 10

it_companies[0]=it_companies[0].upper()
print(it_companies)

#Exercise 11

it_companies.insert(7, 'Tesla')
print(it_companies)

#Exercise 12

it_companies.insert(4, 'Python')
print(it_companies)

#Exercise 13

it_companies[1]=it_companies[1].upper()
print(it_companies) 

#Exercise 14

joined_companies = '# '.join(it_companies)
print(joined_companies)

#Exercise 15

does_exist = 'Python' in it_companies
print(does_exist)

#Exercise 16

it_companies.sort()
print(it_companies)

#Exercise 17

it_companies.reverse()
print(it_companies)

#Exercise 18

first_three = it_companies[:-3]
print(first_three)

#Exercise 19

last_three = it_companies[-3:]
print(last_three)

#Exercise 20

middle_three = it_companies[1:6]
newlist= [company for company in it_companies if len(company) > 6]
print(newlist)