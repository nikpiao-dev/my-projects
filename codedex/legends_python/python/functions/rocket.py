"""
Instructions
In September 1999, after ten months of travel to Mars, the Mars Climate Orbiter suddenly burned to pieces because it had entered the atmosphere too fast.

Oh no! The NASA engineers forgot to convert imperial data to metric data in one of the functions! This noob mistake cost American taxpayers $125 million total.

Suppose you're a NASA intern, and your team is calculating the distance a rocket needs to travel. The value calculated is in kilometers, while the next step requires miles. Your manager quickly writes this on the board:


miles= 
1.609
kilometer
​
 

Create a new file called rocket.py.

Define a function named distance_to_miles() that converts a distance from kilometers to miles. It should:

Take in one parameter named distance (the distance in kilometers).
Print the distance in miles.
After, call the function and use 10000 as the argument.

"""


# def distance_to_miles(distance):
  # miles = distance / 1.609
  # print(miles)

# distance_to_miles(1000)


# def distance_to_miles(distance):
  # return distance / 1.609
# answer = distance_to_miles(1000)
# print(answer)
# distance_to_miles(1000)

def distance_to_miles(distance):
  miles = distance / 1.609
  return miles

print(distance_to_miles(1000))


