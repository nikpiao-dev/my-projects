"""
Instructions
Ever wonder how many people live in New York City? What about London?

Create a favorite_cities.py program.

Let's make a City class that uses the __init__() method to define the following attributes:

name (string)
country (string)
population (integer rounded to the nearest thousand people)
landmarks (list of strings)
Next, create an object for your hometown and assign the attributes above.

Lastly, create another object for the city that you've always wanted to visit!

Bonus: Add 2-3 more attributes, like nickname, founding year, mayor, etc.
"""



class City:
    def __init__(self, name, country, population, landmarks, founding_year, mayor):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks
        self.founding_year = founding_year
        self.mayor = mayor

# Create City objects
tampa = City(
    name="Tampa",
    country="USA",
    population=395000,
    landmarks=["Tampa Riverwalk", "Busch Gardens", "Ybor City"],
    founding_year=1823,
    mayor="Jane Castor"
)

seattle = City(
    name="Seattle",
    country="USA",
    population=737000,
    landmarks=["Space Needle", "Pike Place Market", "Chihuly Garden and Glass"],
    founding_year=1851,
    mayor="Bruce Harrell"
)

new_york = City(
    name="New York",
    country="USA",
    population=8419000,
    landmarks=["Statue of Liberty", "Central Park", "Empire State Building"],
    founding_year=1624,
    mayor="Eric Adams"
)

print(vars(tampa))
print()
print(vars(seattle))
print()
print(vars(new_york))
print()



