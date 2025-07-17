"""
Instructions
In the last exercise, we created a Restaurant class.

In a new file called bobs_burgers.py, create an instance of the Restaurant class called bobs_burgers with the following attributes:

'Bob\'s Burgers'
'American Diner'
4.7
False
Once you do that, create two more instances of the Restaurant class with your favorite dinner spots nearby.

Then, use print(vars()) to output each of the three restaurants!

"""


class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = True

bobs_burgers = Restaurant()
sunny_sushi = Restaurant()
pasta_palace = Restaurant()

# first instance
bobs_burgers.name = "Bob's Burgers"
bobs_burgers.category = "American Diner"
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

# second instance
sunny_sushi.name = "Sunny Sushi"
sunny_sushi.category = "Japanese"
sunny_sushi.rating = 4.5
sunny_sushi.delivery = True

# third instance
pasta_palace.name = "Pasta Palace"
pasta_palace.category = "Italian"
pasta_palace.rating = 4.9
pasta_palace.delivery = False


print(vars(bobs_burgers))
print(vars(sunny_sushi))
print(vars(pasta_palace))

