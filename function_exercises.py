# Exercises
# Create a file named function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.
# 1. Define a function named is_two. It should accept one input and return True if the passed 
# input is either the number or the string 2, False otherwise.
def is_two(x):
    if x == 2 or x == '2':
        return True
    return False
# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, 
# False otherwise.
vowel = ["a" , "e" , "i" , "o" , "u"]

def is_vowel(word):
    word = word.lower()
    if word[0] in vowel and len(word)<=1:
        return True
    return False
# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.
# using the is_vowel function, and ASSUMMMING the string ONLY contains letters
# we could solve as follows:
def is_consonant(word):
    word = word.lower()
    if word[0] not in vowel and len(word) <= 1:
        return True
    return False
# this works on all strings, not just letters
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

def is_consonant(word):
    word = word.lower()
    if word[0] in consonant and len(word) <= 1:
        return True
    return False

# if we wanted to use is_vowel function, we could do so like:
vowel = ["a" , "e" , "i" , "o" , "u"]
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def is_consonant(word):
    word = word.lower()
    if word[0]  not in vowel and len(word)<=1 and word in alpha:
        return True
    return False

# and now that I know about .isalpha()...

vowel = ['a', 'e', 'i', 'o', 'u']
def is_consonant(word):
    word = word.lower()
    if word[0].isalpha() and word[0] not in vowel and len(word) <= 1:
        return True
    return False


# 4.    Define a function that accepts a string that is a word. The function should capitalize the 
#       first letter of the word if the word starts with a consonant.

vowel = ['a', 'e', 'i', 'o', 'u']

def is_consonant(word):
    word = word.lower()
    if word.startswith(tuple(vowel)):
        return word
    else:
        return word.capitalize()

# 5.    Define a function named calculate_tip. It should accept a tip percentage (a number between 0 
#       and 1) and the bill total, and return the amount to tip.

def calculate_tip(bill_total, tip_percentage):
    bill_total = float(bill_total)
    tip_percentage = float(tip_percentage)
    
    return bill_total * tip_percentage

# 6.    Define a function named apply_discount. It should accept a original price, and a discount 
#       percentage, and return the price after the discount is applied.
# this works if the discount is input as a number between 0 and 1
def apply_discount(original_price, discount_percentage):
    original_price = float(original_price)
    discount_percentage = float(discount_percentage)
    return  (original_price - original_price * discount_percentage)

# this works if discount is input as an integer between 0 and 100
def apply_discount(original_price, discount_percentage):
    original_price = float(original_price)
    discount_percentage = float(discount_percentage) / 100
    return  (original_price - original_price * discount_percentage)

# 7.    Define a function named handle_commas. It should accept a string that is a number that contains 
#       commas in it as input, and return a number as output.

def handle_commas(string):
    new_string = float(string.replace(',', ''))
    return new_string

# 8. Define a function named get_letter_grade. It should accept a number and 
# return the letter grade associated with that number (A-F).

def get_letter_grade(report):
    if report < 70:
        return 'F'
    elif report < 75:
        return 'D'
    elif report < 80:
        return 'C'
    elif report < 90:
        return 'B'
    elif report < 100:
        return 'A'
    elif report == 100:
        return 'Perfect Score'
    elif report > 100:
        return 'Bonus Points!!!'

# 9.    Define a function named remove_vowels that accepts a string and returns a string with all the 
#       vowels removed.

def remove_vowels(string):
    for x in string:
        if x in vowel:
            string = string.replace(x, '')
    return string

# 10.   Define a function named normalize_name. It should accept a string and return a valid python 
#       identifier, that is:
#       - anything that is not a valid python identifier should be removed
#       - leading and trailing whitespace should be removed
#       - everything should be lowercase
#       - spaces should be replaced with underscores
#       - for example:
#           - Name will become name
#           - First Name will become first_name
#           - % Completed will become completed

# def get_valid_string(string):
#     return ''.join([c for c in string if c.isalnum() or c == ' ' or c == '_'])

# def remove_first_digit(string):
#     for x in  string:
#         if x == '_' or x.isalpha():
#             return string
#         else:
#             string = string[1:]
#     return string
        
# def normalize_name(string):
#     valid_string = remove_first_digit(string)
#     return valid_string.lower().strip().replace(' ','_')

# with Chad and John's help...

# def normalize_name(word):
    
# # creating an empty string
#     characters = ' '
    
# # removing special symbols    
#     for letter in word:
#         if letter.isalnum() or letter == ' ' or letter == '_':
#             characters += letter
            
# #checking first character for digits, and removing
#     while characters[0].isdigit():
#         characters = characters[1:]
        
# #stripping whitespace, making lowercase, replacing empty space w/ underscore
#     characters = characters.strip().lower().replace(' ', '_')
#     return characters

# normalize_name('9&123ascd -asd867%')

# this is a cleaner version, that includes th .isidentifier()

def normalize_name(string):
    output = ""
    
    # lowercase all the things
    string = string.lower()

    # Filter out any non-valid identifiers, keep spaces to turn into _
    for character in string:
        if character.isidentifier() or character == " ":
            output += character
    
    # remove any leading or trailing spaces
    output = output.strip()
    
    # replace " " with "_"
    output = output.replace(" ", "_")
    
    return output
# 11.   Write a function named cumulative_sum that accepts a list of numbers and returns a list that 
#       is the cumulative sum of the numbers in the list.
#       - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#       - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(numbers):
    sums = []
    total = 0
    for number in range(0, len(numbers)):
        total += list[number]
        sums.append(total)
    return sums
# 
# Additional Exercise
# 
# - Once you've completed the above exercises, follow the directions from 
# https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 
# in order to thouroughly comment your code to explain your code.
# 
# Bonus
# 
# 1.    Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm 
#       and return a string that is the representation of the time in a 24-hour format. Bonus write a 
#       function that does the opposite.
# 2.    Create a function named col_index. It should accept a spreadsheet column name, and return the 
#       index number of the column.
#       - col_index('A') returns 1
#       - col_index('B') returns 2
#       - col_index('AA') returns 27