"""

Instructions
If you’ve ever signed up for Discord or Reddit, you probably got a random username. Odds are those sites are using list comprehensions to generate fantastical names for new users.

Let’s generate our usernames with functional programming! Here's some code to get us started:

import random

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

Each name will be a combination of a prefix and a suffix randomly chosen from predefined lists.

Under the suffixes list, define a capitalize_suffix() function that returns a capitalized name parameter. Then, use the map() function to apply capitalize_suffix() to each item in the suffix list and store in a variable.

Note: Remember to use the list() function (e.g., list(map(capitalize_suffix, suffixes))).

Next, use list comprehensions to generate 10 fantasy names, using create_fantasy_name(). Save to a new random_names list.

Then, define the following pure functions:

fire_in_name(name) that returns True if 'Fire' is in name.
concatenate_names(name1, name2) that returns a string of name1 + name2.
Next, do the following:

Use filter() and apply fire_in_name() to the random_names list.
Use reduce() and apply concatenate_names() to the filtered names.
Note: Don't forget that we need the functools module to use reduce().

Lastly, define one more pure function, display_name_info(), that does the following:

Prints the generated fantasy names with a for loop.
Prints the filtered names that include 'Fire'.
Prints the reduced names.
Go ahead and use display_name_info(). What names did you get?

"""


import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(name):
  return name.upper()

uppercase_suffixes = list(map(capitalize_suffix, suffixes))


def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

random_names = [
  create_fantasy_name(prefixes, uppercase_suffixes)
  for name in range(10)  
]

def concatenate_names(name1, name2):
  return f"{name1} {name2}"

def fire_in_name(name):
  return 'FIRE' in name  

filtered_names = list(filter(fire_in_name, random_names))

if filtered_names:
  reduced_names = reduce(concatenate_names, filtered_names)
else:
  reduced_names = "No names with 'FIRE'"


def display_name_info(random_names, filter_names, concat_names):
  print("Fantasy Names:")
  for names in random_names:
    print(names)
  
  print("Filtered names with 'Fire': ", filter_names)
  print("Concatenated names: ", concat_names)


display_name_info(random_names, filtered_names, reduced_names)

