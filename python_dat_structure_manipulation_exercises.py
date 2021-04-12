student = students[0]

# 1. How many students are there?
count = 0

for student in students:
    count += 1
    
print(count)

# 2. How many students prefer light coffee? For each type of coffee roast?
# 3. How many types of each pet are there?

horses = []
dogs = []
cats = []
for student in students:
    pets = student['pets']
    for species in pets:
        pet_species = species['species']
        if pet_species == 'horse':
            horses.append(pet_species)
        elif pet_species = 'dog':
            dogs.append(pet_species)
        elif pet_species = 'cat':
            cats.append(pet_species)
print(f'horses = {len(horses)}')
print(f'dogs = {len(dogs)}')
print(f'cats = {len(cats)}')
# 4. How many grades does each student have? Do they all have the same number of grades?

for student in students:
    print(student['student'], 'has', len(student['grades']), 'grades.')
print('\nAll students have', len(student['grades']), 'grades.')

# 5. What is each student's grade average?
for student in students:
    print(student['student'], "'s grade averager is ", sum(student['grades']) / len(student['grades'])))))


# 6. How many pets does each student have?
for student in students:
    print(student['student'], 'has', len(student['pets']), 'pets.')

# 7. How many students are in web development? data science?

web = 0
data = 0
for student in students:
    if student['course'] == 'web development':
        web += 1
    elif student['course'] == 'data science':
        data += 1
print(f'Web Development has {web} students.')
print(f'Data Science has {data} students.')

# 8. What is the average number of pets for students in web development?

web = 0
pets = 0
for student in students:
    if student['course'] == 'web development':
        web += 1
        pets += len(student['pets'])
print('Web Develpoment students have an average of ', (pets / web), ' pets.')

# 9. What is the average pet age for students in data science?

total_age = 0
number_pets = 0

for student in students:
    if student['course'] == 'data science':
        pets = student['pets']
        for pet in pets:
            total_age += pet['age']
            number_pets += 1
average = total_age / number_pets            
print(f'The average pet age for data science students is {average}.')



# 10. What is most frequent coffee preference for data science students?

light_count = 0
medium_count = 0
dark_count = 0

for student in students:
    if student['course'] == 'data science':
        if student['coffee_preference'] == 'light':
            light_count += 1
        elif student['coffee_preference'] == 'medium':
            medium_count += 1
        elif student['coffee_preference'] == 'dark':
            dark_count += 1
            
coffee_choices = {'light': light_count, 'medium': medium_count, 'dark': dark_count}
most_common = max(coffee_choices, key =coffee_choices.get)
print(f'light = {light_count}')
print(f'medium = {medium_count}')
print(f'dark = {dark_count}')
print(f'The most preferred type of coffee for DS studennts is {most_common}.')

# 11. What is the least frequent coffee preference for web development students?

light_list= []
medium_list=[]
dark_list= []
for student in students:
    if student['course']== 'web development':
        if student.get("coffee_preference")== "light":
            light_list.append(student)
            light= len(light_list)
        elif student.get("coffee_preference")== "medium":
            medium_list.append(student)
            med= len(medium_list)
        elif student.get("coffee_preference")== "dark":
            dark_list.append(student)
            dark= len(dark_list)
            
for coffee in student:
    if light < med and light < dark:
        print("Least frequent coffee is light")
    else:
        pass
    if light == med:
        print("Least frequent coffee is light and medium")
    else:
        pass
    if light == dark:
        print("Least frequent coffee is light and dark")
    else:
        pass
    if med < light and med < dark:
        print("Least frequent coffee is medium")
    else:
        pass
    if med == dark:
        print("Least frequent coffee is medium and dark")
        break
    else: 
        pass
    if dark < light and dark < med:
        print("Least frequent coffee is dark")
    else:
        print("Error")

# 12. What is the average grade for students with at least 2 pets?

grades_list = []
for student in students:
    if len(student['pets']) >= 2:
        grades_list.extend(student['grades'])
print('The average grade of studnets with at least two pets is', mean(grades_list))

# 13. How many students have 3 pets?

three_pets = []
for student in students:
    if len(student['pets']) == 3:
        three_pets.append(student)
        amt_of_pets = len(three_pets)
print(f'The amount of students who have 3 pets is : {amt_of_pets}')

# 14. What is the average grade for students with 0 pets?

grades_list = []
for student in students:
    if len(student['pets']) == 0:
        grades_list.append(student['grades'])
print('The average grade of students w/o pets is', mean(grades_list))

# 15. What is the average grade for web development students? data science students?

g_list = []
for student in students:
    if student['course'] == 'web development':
        g_list.extend(student['grades'])
print('The average grade of WebDev students is', mean(g_list))

gr_list = []
for student in students:
    if student['course'] == 'data science':
        gr_list.extend(student['grades'])
print('The average grade of DS students is', mean(gr_list))

# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?

grd_list = []
max_grade = max(grd_list)
min_grade = min(grd_list)
for student in students:
    if student['coffee_preference'] == 'dark':
        grd_list.append(student['grades'])

print(f'The grade range for dark coffee drinkers goes from {min_grade} to {max_grade}.')


# 17. What is the average number of pets for medium coffee drinkers?
# 18. What is the most common type of pet for web development students?
# 19. What is the average name length?
# 20. What is the highest pet age for light coffee drinkers?