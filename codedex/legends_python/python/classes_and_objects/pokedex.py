"""
Instructions
Since 1996, the Pokémon video game franchise has delighted players around the world with collectible pocket monsters. A Pokédex is a device that tracks the information for Pokémon that are seen or caught.

Create a new file called pokedex.py.

Next, let's define a Pokemon class with the following attributes:

entry (integer)
name (string)
types (list of strings)
description (string)
is_caught (boolean)
Note: Make sure to use the __init__() method.

Next, create an instance method called .speak() that prints a string of the sound a Pokémon makes. A Pokémon usually just says their name, so make the .speak() simply print out their name twice!

Then, create another instance method called .display_details() that prints the attributes of a Pokemon object like the following:

Entry Number: 25
Name: Pikachu
Type: Electric
Description: It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.
Pikachu has already been caught!

Lastly, create three Pokemon class objects and use the .speak() or .display_details() instance methods for each one.

For more information about any Pokémon you want to add, see the Pokédex!

Are you ready to earn the next badge?

Bonus: For all the super fans, try and add more attributes to the Pokemon class definition, like level, region, height, or weight.

"""


class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self, sound):
    return sound * 2;

  # def display_detail(self):
  #    def display_details(self):
  #   print('Entry Number: ' + str(self.entry))
  #   print('Name: ' + self.name)

  #   if len(self.types) == 1:
  #     print('Type: ' + self.types[0])
  #   else:
  #     print('Type: ' + self.types[0] + '/' + self.types[1])
    
  #   print('Description: ' + self.description)

  #   if self.is_caught:
  #     print(self.name + ' has already been caught!')
  #   else:
  #     print(self.name + ' hasn\'t been caught yet.')

  def display_details(self):
    print("Entry number: " , self.entry)
    print("Name: ", self.name)
    print("Type: ", self.types)
    print("Description: ", self.description)
    if self.is_caught == True:
      print(self.name + "has already been caught!")
    else:
      print(self.name + "has not been caught yet.")
  

bulbasaur = Pokemon(1, "Bulbasaur", ["Grass", "Poison"], "It has a plant bulb on its back that stores energy and grows as it absorbs sunlight. As it evolves, the bulb blooms into a large flower.", True)
magnemite = Pokemon(81, "Magnemite", ["Electric", "Steel"], "It generates powerful electromagnetic fields, which can cause metal objects to be attracted to it.", False)
sneasel = Pokemon(215, "Sneasel", ["Dark", "Ice"], "It’s known for its agility and is often found in icy, mountainous areas. Sneasel is skilled in sneaking around, and it uses its claws to climb and slash opponents.", True)

print(bulbasaur.speak("bulba"))
print()
bulbasaur.display_details()
print()

print(magnemite.speak("Bzzzt!"))
print()
magnemite.display_details()
print()

print(sneasel.speak("Krii"))
print()
sneasel.display_details()

