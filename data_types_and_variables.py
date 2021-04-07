## rented 3 different movies
## each rented for a differnt amount of time
## each cost same amount per day
## how much is total cost?


the_little_mermaid = {
    "name": "The Little Mermaid",
    "days_rented": 3,
    "dollars_per_day": 3
}
the_little_mermaid

brother_bear = {
    "name": "Brother Bear",
    "days_rented": 5,
    "dollars_per_day": 3
}
brother_bear

hercules = {
    "name": "Hercules",
    "days_rented": 1,
    "dollars_per_day": 3
}

hercules

movie_rentals = [the_little_mermaid, brother_bear, hercules]

print(movie_rentals)

print(movie_rentals["the_little_mermaid"][1]) 

print(the_little_mermaid["days_rented"])

movie_rentals = {the_little_mermaid, brother_bear, hercules}

## giving up on this method for now due to time constraints
## will re-attempt once I am more comfortable w/ Python

## here is my quick(er) way of solving this problem

You have rented some movies for your kids: The little mermaid (for 3 days), 
Brother Bear (for 5 days, they love it), and Hercules 
(1 day, you don't know yet if they're going to like it). 
If price for a movie per day is 3 dollars, how much will you have to pay?

## The Little Mermaid rented for 3 days
a = 3
## Brother Bear rented for 5 days
b = 5
## Hercules rented for 1 day
c = 1
## Testing my variables
print(a + b + c)
## Create New Variable for Total Number of Rental Days
total_rental_days = a + b + c
## Testing new variable
print(total_rental_days)
## Creating cost variable (even though it is constant here, this will allow easier updates)
cost_per_day = 3
## testing variable
print(cost_per_day)
## put it all together
total_cost = total_rental_days * cost_per_day
## did it work?
print(total_cost)
## of course it did
## 27 dollars

## Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
## they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, 
## and Facebook 350. How much will you receive in payment for this week? 
## You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

## 3 compaines with 3 different pay rates, and 3 different number of hours worked
## how much TOTAL earned this week?

## setting variables for each payrate
gp = 400
ap = 380
fp = 350
## setting variables for each work hours
gw = 6
aw = 4
fw = 10
## setting variable for total at each company
## this is unneccessary, but will provide greater context/insight
google = gp * gw
amazon = ap * aw
facebook = fp * fw
## checking the math on each company
print(google)
print(amazon)
print(facebook)
## put it all together 
total_earned = google + amazon + facebook
print(total_earned)
## 7420 dollars earned this week between 3 companies

## A student can be enrolled to a class only if the class is not full and the class schedule 
## does not conflict with her current schedule.

## create variables to determine if class is full
is_full = False
conflict = False
## create new variable to see if they can enroll - they can
## well this didn't work at all
def can_enroll(is_full, conflict):
    if not is_full and not conflict:
        return True
    else:
        return False

## let's try another method
is_full = False
conflict = False

enrollable_status = not (is_full or conflict)
print(enrollable_status)

# A product offer can be applied only if people buys more than 2 items, and the offer 
# has not expired. Premium members do not need to buy a specific amount of products.

more_than_two_items = True
offer_not_expired = True
premium_membership = False
discount_eligible = offer_not_expired and (more_than_two_items or premium_membership)
print(discount_eligible)

# Use the following code to follow the instructions below:

# username = 'codeup'
# password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:

# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

pw_len_suff = len(password) >= 5
usr_len_suff = len(username) <= 20
pw_not_usr = username != password

usr_and_pw_valid = pw_len_suff and usr_len_suff and pw_not_usr

print(usr_and_pw_valid)