print("Hello, World!")
print(len("Hello, World!"))
print(type("Hello, World!"))
print(str(10))
print(int(10))
print(float(10))


first_name = (input("enter your name: "))
last_name = "González"
country = "Mexico"
city = "Aguascalientes"
age = (input("enter your age: "))
is_married = False
skills = ["HTML", "CSS", "JS", "Python"]
person_info = {
  "first_name": first_name,
   "last_name": last_name,
   "country": country,
    "city": city,
    "age": age,
   "is_married": is_married,
    "skills": skills
}
print("Hello,", first_name)
print("First name:", first_name)
print("Last name:", last_name)
print("Country:", country)
print("City:", city)
print("Age:", age)
print("Is married:", is_married)
print("Skills:", skills)
print("Person info:", person_info)

print(first_name, last_name, country, city, age, is_married)


#2.2 - 2.3

print(len(first_name))
print(len(last_name))

#Excersise 2.4

print(len(first_name) > len(last_name))
print(len(first_name) < len(last_name))
print(len(first_name) == len(last_name))
print(len(first_name) != len(last_name))
print(len(first_name) >= len(last_name))
print(len(first_name) <= len(last_name))

#Excersise 2.5

num_one = 5
num_two = 4

#Excersise 2.6 - 2.11

Total= int(num_one + num_two)
Difference= int(num_one - num_two)
Product= int(num_one * num_two)
Division= int(num_one / num_two)
Remainder= int(num_one % num_two)
Exp= int(num_one ** num_two)
Floor_division= int(num_one // num_two)

print('Total:', Total)
print('Difference:', Difference)
print('Product:', Product)
print('Division:', Division)
print('Remainder:', Remainder)
print('Exp:', Exp)
print('Floor division:', Floor_division)

#Excersise 2.12

Radius= int(30)
Area_of_circule= int(3.14 * Radius ** 2)  
Circum_of_circule= int(2 * 3.14 * Radius)
print('Area of a circle:', Area_of_circule)
print('Circumference of a circle:', Circum_of_circule)

#Excersise 2.13

print("\nUser Information:")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Country: {country}")
print(f"Age: {age}")

#Excersise 2.14

help('keywords')
