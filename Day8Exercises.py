#Exercise 1
dog = dict()
#Exercise 2
dog = {"name": "Bruno", "color": "Black", "breed": "pug", "legs": 4, "age": 4}
#Exercise 3
student_dictionary = {
    "first_name": "Diego",
    "last_name": "Garduño González",
    "gender": "Male",
    "age": 18,
    "marital_status": "Single",
    "skills": ["procrastinating"],
    "country": "Mexico",
    "city": "Aguascalientes",
    "address": "Calle Carlos M. Bustamante, Colonia Morelos II, Numero 326",
}
#Exercise 4

print(len(student_dictionary))
#Exercise 5

print(student_dictionary["skills"])
print("Valor de skills:", student_dictionary["skills"])
print(type(student_dictionary["skills"]))
#Exercise 6

student_dictionary["skills"].append("Sleeping")
#Exercise 7

list_keys = list(student_dictionary.keys())
#Exercise 8

list_values = list(student_dictionary.values())
#Exercise 9

list_of_tuples = [(k, v) for k, v in student_dictionary.items()]
#Exercise 10

student_dictionary.pop("marital_status")
#Exercise 11

del dog