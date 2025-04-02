#Level 1

# Exercise 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercise 2
print("Length of set is :", len(it_companies))

#Exercise 3
it_companies.add('Twitter')
print(it_companies)

#Exercise 4
it_companies.update(['Infosys', 'Firmonyx'])
print(it_companies)

#Exercise 5
it_companies.remove('Facebook')
print(it_companies)

#Level 2

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#Exercise 1
C = A.union(B)
print(C)

#Exercise 2
C = A.intersection(B)
print(C)

#Exercise 3
print("Is A subset of B : ", A.issubset(B))

#Exercise 4
print("Are A and B disjoint sets : ", A.isdisjoint(B))

#Exercise 5
C = A.union(B)
D = B.union(A)
print("A U B" , C)
print("B U A", D)

#Exercise 6
C = A.symmetric_difference(B)
print("Symmetric difference between A and B", C)

#Exercise 7
del A
del B

#Level 3

#Exercise 1
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercise 2
age_set = set(age)
len_list = len(age)
len_set = len(age_set)
print("Length of list : ", len_list)
print("Length of set : ", len_set)
print("Length of list is bigger than length of set : ", len_list > len_set)

#Exercise 3

str = "I am a teacher and I love to inspire and teach people"
splitted_string = str.split()
unique_words = set(splitted_string)
print(splitted_string)
print(unique_words)
print("Unique words in string : ", len(unique_words))