# New line function
def n1():
    print('\n')



# Tuples - collection of ordered items / elements similar to a list
    # However, Immutable (cannot be changed) - uses () instead of []


coordinates = (40.7128, 74.0060) # New York
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
student = ('John Doe', 8675309, 'Computer Science') # Tuples can store mixed types

print(student[1])

# student.pop()
# print(student)

tup = () #empty tuple

tup = (1, 2, 3)

print(type(tup)) # <class 'tuple'>
print(isinstance(tup, tuple)) # => True
print(len(tup))


tup[:2] # => (1, 2)
print(2 in tup) # True
print("tup:", tup)

new_tup = tup + (4, 5, 6) # creates a new tuple, but doesn't store it
print("new_tup:", new_tup) # (1, 2, 3, 4, 5, 6)

# or

# tup = tup + (4, 5, 6)







n1()