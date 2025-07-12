"""
Instructions
Fortune Cookie is a small cookie wafer with a piece of paper inside, called a “fortune”, which is usually a Chinese phrase with translation and a list of lucky numbers. They are served in restaurants in the U.S. and Canada. 🥠

Create a fortune_cookie.py program that gives the user random fortunes.

Define a function named fortune(). Inside the function, print out a random fortune from the list of options below:

Don't pursue happiness – create it.
All things are difficult before they are easy.
The early bird gets the worm, but the second mouse gets the cheese.
Someone in your life needs a letter from you.
Don't just think. Act!
Your heart will skip a beat.
The fortune you search for is in another cookie.
Help! I'm being held prisoner in a Chinese bakery!
Make sure to use the random module's random.randint() and an if/elif/else.

Then, call the fortune() function three times and see what you get!

Bonus: If you're daring, rewrite the function without an if/elif/else.

"""


import random

# def fortune():
#   random_fortune = random.randint(0, 8)
  
#   if random_fortune == 1:
#     return "Don't pursue happiness – create it"
#   elif random_fortune == 2:
#     return "All things are difficult before they are easy"
#   elif random_fortune == 3:
#     return "The early bird gets the worm, but the second mouse gets the cheese"
#   elif random_fortune == 4:
#     return "Someone in your life needs a letter from you."
#   elif random_fortune == 5:
#     return "Don't just think. Act"
#   elif random_fortune == 6:
#     return "Your heart will skip a beat."
#   elif random_fortune == 7:
#     return "The fortune you search for is in another cookie"
#   elif random_fortune == 8:
#     return "Help! I'm being held prisoner in a Chinese bakery!"
#   else:
#     return "Sorry, no fortune for you today."

options = [
  'Don’t pursue happiness – create it.',
  'All things are difficult before they are easy.',
  'The early bird gets the worm, but the second mouse gets the cheese.',
  'If you eat something and nobody sees you eat it, it has no calories.',
  'Someone in your life needs a letter from you.',
  'Don’t just think. Act!',
  'Your heart will skip a beat.',
  'The fortune you search for is in another cookie.',
  'Help! I’m being held prisoner in a Chinese bakery!'
]
def fortune():
  random_fortune = random.randint(0, len(options) - 1)
  print(options[random_fortune])

fortune()
fortune()
fortune()
