"""
Instructions
Let's start a book club by making a list of popular books! 📚

Create a reading_list.py program that stores the following items in a books list:

'Harry Potter'
'1984'
'The Fault in Our Stars'
'The Mom Test'
'Life in Code'
Suppose we want to add 'Pachinko' to the list. Can you use a list method to do so?

Let's say we finished reading 'The Fault in Our Stars' and '1984'. Can you use the .remove() method to remove one and the .pop() method to remove the other?

Print the updated list out to make sure everything's good to go!

"""


books = ['Harry Potter', '1984', 'The Fault in Our Stars', 'The Mom Test', 'Life in Code']


print("Original list:", books)
print()

# add pachinko

books.append("Pachinko")
books.remove('The Fault in Our Stars')
books.pop(1)


print("Updated list:", books)
print()

