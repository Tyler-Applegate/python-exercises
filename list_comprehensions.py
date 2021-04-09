# list comprehension exercises

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]    

# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable 
# named uppercased_fruits to hold the output of the list comprehension. Output should be 
# ['MANGO', 'KIWI', etc...]

uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to 
# produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

### what do I need to do to get Mandarin orange to print Mandarin Orange?????

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
# Hint: You'll need a way to check if something is a vowel.

vowel = ['a', 'e', 'i', 'o', 'u']

fruit_test = 'mango'

print(len([char for char in fruit_test.lower() if char in vowel]))

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if len([char for char in fruit if char in vowel]) > 2]
print(fruits_with_more_than_two_vowels)

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

fruits_with_only_two_vowels = [fruit for fruit in fruits if len([char for char in fruit if char in vowel]) == 2]
print(fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters

more_than_5_char = [fruit for fruit in fruits if len(fruit) > 5]
print(more_than_5_char)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

exactly_5_char = [fruit for fruit in fruits if len(fruit) == 5]
print(exactly_5_char)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

less_than_5_char = [fruit for fruit in fruits if len(fruit) < 5]
print(less_than_5_char)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

char_count = [len(fruit) for fruit in fruits]
print(char_count)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

odd_numbers = [n for n in numbers if n % 2 != 0]
print(odd_numbers)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

positive_numbers = [n for n in numbers if n > 0]
print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

negative_numbers = [n for n in numbers if n < 0]
print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

multinumeral = [n if (n < 0 and len(str(n)) > 2) else n for n in numbers if len(str(n)) > 1]
print(multinumeral)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

numbers_squared = [n ** 2 for n in numbers]
print(numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

odd_negative_numbers = [n for n in numbers if n < 0 and n % 2 !=0]
print(odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

numbers_plus_5 = [n + 5 for n in numbers]
print(numbers_plus_5)

# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. 
# *Hint* you may want to make or find a helper function that determines if a given number is prime or not.



