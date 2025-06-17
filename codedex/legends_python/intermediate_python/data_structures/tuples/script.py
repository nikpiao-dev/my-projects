"""
Instructions:

Thanks to the internet, we can connect with friends across the world. 🧑‍🤝‍🧑

When you and your friends are scattered across different cities, sharing locations is something that can help you feel closer. 🫶

Let's use latitude and longitude 🌐 to create tuples of our friends locations!

Create a tuple for the city you are in.
Create 3 tuples for your friends, each with the latitude and longitude of the cities they live in.
Print the locations of all your friends.
Which of your friends is the furthest away?

Hit "Complete" to feel closer than ever with your friends. 🥰

Bonus: See if you can combine all the tuples into one tuple.

"""


my_latitude = '27.9506° N',
my_longitude = '82.4572° W',

my_city = my_latitude + my_longitude
print(f"My city's latitude is: {my_latitude} and longitude is: {my_longitude}.")
print()

peter_city = ('33.0472° S', ' 71.6127° W')
jane_city = ('64.1466° N', '21.9426° W')
hiro_city = ('35.0116° N', '135.7681')

print(f"Peter's city latitude is: {peter_city[0]} and longitude is {peter_city[1]}.")
print(f"Jane's city latitude is: {jane_city[0]} and longitude is {jane_city[1]}.")
print(f"Hiro's city latitude is: {hiro_city[0]} and longitude is {hiro_city[1]}.")
print()

print(f"My city is Tampa.")
print(f"Peter's city is Valparaíso.")
print(f"Jane's city is Reykjavík.")
print(f"hiro's city is Kyoto.")
print()

print("Jane's city is the most closest city from Tampa is Reykjavík, which is estimated to be ~5,824 km away.")
print("Hiro's city of Kyoto is the farthest from Tampa, which is estimated to be ~11,966 km away.")
print()

# Combine all friends' locations and Define each friend's location as a string

friend1_location = 'Valparaíso: 33.0472° S, 71.6127° W'
friend2_location = 'Reykjavík: 64.1466° N, 21.9426° W'
friend3_location = 'Kyoto: 35.0116° N, 135.7681° E'

# Combine them into one string
all_friends_locations = friend1_location + " | " + friend2_location + " | " + friend3_location

# Print
print("All friends' locations combined:", all_friends_locations)
