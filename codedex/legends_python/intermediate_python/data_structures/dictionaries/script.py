"""
Instructions:

🍎 Welcome to NYC! 🗽

As one of the cultural capitals of the world, NYC is the home of the Met Museum.

It has one of the biggest art collections in the world! 🗺️

Let’s catalog an artifact from the museum! 🖼️ 👩‍🎨

First, search the Met Museum site for your favorite artifact. Scroll to "Artwork Details" and let's start cataloging.

On the Python editor, create a dictionary with the information of your artifact, including:

artist
period
date
Lastly, print the dictionary. What do you see? What if we just want to print the keys, or the values?


Hint:
# This dictionary represents a Terracotta Pyxis box
pyxis = {
  'artist': 'Penthesilea painter',
  'period': 'classical',
  'date': '465-460 BCE'
}

"""

# dictionary about hanging scroll (example):

hanging_scroll = {
  'title': "Spring Dawn over the Elixir Terrace",
  'artist':"Lu Guang",
  'period': "early Ming dynasty",
  'date': "ca. 1369",
  'culture': "China",
  'medium': "Ink on paper",
  'classification': "Paintings"
}

print('\nKeys:', hanging_scroll.keys())
print()
print('\nValues:', hanging_scroll.values())
print()
print('\nItems:', hanging_scroll.items())

# Dictionary representing a Pyxis (with some extra info)
pyxis = {
  'artist': 'Penthesilea painter',
  'period': 'classical',
  'date': '465-460 BCE',
  'culture': ['Greek', 'Attic'],
  'medium': ['terracotta', 'white-ground'],
  'dimensions': {'height': '4.75in', 'height w/cover': '6.75in'}
}

print('Printing the dictionary: ', pyxis)
print('\nPrinting the keys: ', pyxis.keys())
print('\nPrinting the values: ', pyxis.values())
