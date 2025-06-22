"""

Instructions:

With sets, you are one step closer to becoming a Python Data Manipulator. 🧗

🫐🍇🍌 Let’s go back to fruits! 🍓🍒🍎

Grocery shopping is great until you forget what was on your list. 😥

Before you head out, your best friend ask you to pick up some fruit for her too. Let's combine the lists!

Create two sets representing your favorite fruits and your best friend's favorite fruits.
Print the union of the two sets would look like.
Print the intersection of the two sets.
Have fun with it, check if the same fruit is in both sets or see the <difference> in both sets.

Remember: tomatoes are fruits! 🍅

"""



my_fruits = {'Apple 🍎', 'Banana 🍌', 'Grape 🍇', 'Strawberry 🍓'}
friend_fruits = {'Strawberry 🍓', 'Cherry 🍒', 'Blueberry 🫐', 'Banana 🍌'}

union_fruits = my_fruits.union(friend_fruits)
intersect_fruits = my_fruits.intersection(friend_fruits)
diff_fruits = my_fruits.difference(friend_fruits)


print('\nUsing union_set:', union_fruits)
print('\nUsing intersection_set:', intersect_fruits)
print('\nUsing difference_set:', diff_fruits)
