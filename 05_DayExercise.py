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

#Exercise 21

it_companies.pop(0)
print(it_companies)

#Exercise 22
it_companies.pop(4)
print(it_companies)

#Exercise 23

it_companies.pop(6)
print(it_companies)

#Exercise 24 and 25

it_companies.clear()
print(it_companies)

#Exercise 26

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)

#Exercise 27

full_stack = front_end
print(full_stack)


#FASE 2

#Exercise 1

lst = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
lst = lst[::-1]
print(lst)

lst.sort()
min_age = min(lst)
max_age = max(lst)

print("Lista ordenada:", lst)
print("Edad mínima:", min_age)
print("Edad máxima:", max_age)

n = len(lst)
if n % 2 == 0:
    median_age = (lst[n//2 - 1] + lst[n//2]) / 2
else:
    median_age = lst[n//2]

average_age = sum(lst) / n
age_range = max_age - min_age

min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)

print("Lista ordenada:", lst)
print("Edad mínima:", min_age)
print("Edad máxima:", max_age)
print("Edad mediana:", median_age)
print("Edad promedio:", average_age)
print("Rango de edades:", age_range)
print("Diferencia (min - promedio):", min_avg_diff)
print("Diferencia (max - promedio):", max_avg_diff)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

#Exercise 1

n = len(countries)
if n % 2 == 0:
    middle_countries = countries[n//2 - 1:n//2 + 1]
else:
    middle_countries = [countries[n//2]]

print("País(es) del medio:", middle_countries)

#Exercise 2

n = len(countries)
if n % 2 == 0:
    first_half = countries[:n//2]
    second_half = countries[n//2:]
else:
    first_half = countries[:n//2 + 1]
    second_half = countries[n//2 + 1:]

print("Primera mitad:", first_half)
print("Segunda mitad:", second_half)

#Exercise 3

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first, second, third, *scandic_countries = countries

print("Primer país:", first)
print("Segundo país:", second)
print("Tercer país:", third)
print("Países escandinavos:", scandic_countries)

#ya tacosss