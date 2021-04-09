# Python String, List, Dictionary Warmup Exercises
# Write the code that operates on a single string containing the make and model of a vehicle. The first part of the string before the space is the make The last part of the string after the space is the model We can assume that the strings will only have one space. Assume the input string is completely lower-cased.

# Example inputs:

# truck = "toyota tacoma"
# sedan = "hyundai sonata"
# sports_car = "lambourgini diablo"

# Exercise #1
# Write the code to take a string and produce a dictionary out of that string such that the output looks like the following: Some thoughts:

# You'll need a way to get the first part of the string and a way to get the second part of the string
# Feel free to make new variables/data types in between the string and the output dictionary

# Input truck = "toyota tacoma"

# Output

# truck = {
#     "make": "toyota",
#     "model": "tacoma"
# }

# my code goes here:

manumobile = "toyota corolla"
make_and_model = manumobile.split()
make = manumobile.split()[0]
model = manumobile.split()[1]

car_dict = {
    "make": make,
    "model": model
}

print(car_dict)

# Exercise #2
# Write the code that takes a dictionary containing make/model for a vehicle and capitalizes the first character of the make and the model:

# Input

# truck = {
#     "make": "toyota",
#     "model": "tacoma"
# }
# Output

# truck = {
#     "make": "Toyota",
#     "model": "Tacoma"
# }

#my code goes here:

car_dict = {
    "make": make,
    "model": model
}

car_dict["make"] = car_dict["make"].capitalize()
car_dict["model"] = car_dict["model"].capitalize()

print(car_dict)


# Exercise #3
# Create a list of 3 dictionaries where each dictionary represents a vehicle, as above Write the code that operates on that list of dictionaries in order to uppercase the entire make and model values.

# Input

# truck = {
#     "make": "Toyota",
#     "model": "Tacoma"
# }
# Output

# truck = {
#     "make": "TOYOTA",
#     "model": "TACOMA"
# }


truck_list = [
    {
        "make": "Toyota",
        "model": "Tacoma"
    },
    {
        "make": "Toyota",
        "model": "Tundra"
    },
    {
        "make": "Chevy",
        "model": "Silverado"
    }
]

print(truck_list)



for truck in truck_list:
    truck["make"] = truck["make"].upper()
    truck["model"] = truck["model"].upper()

print(truck_list)

