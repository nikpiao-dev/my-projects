"""
Instructions
Create a todo.py program that will define a todo list that contains the following items:

'🏦 Get quarters.'
'🧺 Do laundry.'
'🌳 Take a walk.'
'💈 Get a haircut.'
'🍵 Make some tea.'
'💻 Complete Lists chapter.'
'💖 Call mom.'
'📺 Watch My Hero Academia.'
Print the first item and the second item. What did you get?

Next, use slicing to print the third, fourth, and fifth items.

Try printing out the item at index 9 to see the IndexError before moving on.

"""


todo = [
    "🏦 Get quarters.",
    "🧺 Do laundry.",
    "🌳 Take a walk.",
    "💈 Get a haircut.",
    "🍵 Make some tea.",
    "💻 Complete Lists chapter.",
    "💖 Call mom.",
    "📺 Watch My Hero Academia."
]

print("Todo list:", todo)
print("First item:", todo[0])
print("Second item:", todo[1])
print("Index 2 to Index 4:", todo[2 : 5])
print("Last item", todo[-1])
print("Item at index 9:", todo[9]) # IndexError

