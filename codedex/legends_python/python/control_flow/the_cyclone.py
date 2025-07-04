"""
Instructions
Since 1927, "The Cyclone" roller coaster has delighted visitors at Coney Island (Brooklyn, NY). 🎢

They're now installing a new entry system (the height requirement is 137 cm and the cost is 10 credits) and need your help writing the program for it!

Create a new file called the_cyclone.py.

Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

Use a combination of relational and logical operators to create the rules:

If they are tall enough and have enough credits, print "Enjoy the ride!"
Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."
Else, print a message saying they have not met either requirement.
"""


min_height = 137
min_credits = 10

user_height = int(input("What is your height in cm?: "))
user_credits = int(input("How many credits do you have?: "))
min_height = 137
min_credits = 10

user_height = int(input("What is your height in cm?: "))
user_credits = int(input("How many credits do you have?: "))

if user_height >= min_height and user_credits >= min_credits:
    print('Enjoy the ride!')
elif user_credits >= min_credits and user_height < min_height:
    print('You are not tall enough to ride.')
elif user_height >= min_height and user_credits < min_credits:
    print("You don't have enough credits.")
else:
    print('You are not eligible to go on this ride. Not tall enough and do not have the minimum number of credits needed.')

