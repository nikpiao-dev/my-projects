# Data Structures 
    # - a way for us to store data, retrieve it or process it, etc

def n1():
    print('\n')

# Lists -> Have brackets [] - everything inside is called an item / element

movies = ['Star Trek', 'Harry Potter', 'Tron Legacy', 'The Hobbit: An Unexpected Journey', ]

print(movies[1]) # return the second item in the list - index
print(movies[0]) # index always start at 0 - first item on list

print(movies[1:3]) # return a list 
                   #that start at index 1 and stop before index 3 (exclusive) - ['harry potter', 'tron legacy']

                
print(movies[1:4]) # return items from index 1 - 3
print(movies[1:]) # same as the one above

print(movies[:1]) # prints everything before 1 as a list -> ['Star Trek']

print(movies[-1]) # return the last item in the list

print(len(movies)) # count the items in the list

movies.append('Jaws') # add an item to the list (at the end)
print(movies)

movies.insert(2, 'Interstellar') # insert at a specific position
print(movies) # In this case, inserted at index of 2

movies.pop() # removes the last item
print(movies)

movies.pop(0) # remove the first time, specifically
print(movies)

your_movies = ['Just Go With It', '50 First Dates']

n1()

our_favorites = movies + your_movies
print(our_favorites)


print("=============================================================================")
n1()

# Nested List

grades = [['Bob', 82], ['Alice', 90], ['Jeff', 73]]
bob_grade = grades[0][1]
print("Bob's grade(old):", bob_grade)
print("Old grades: ", grades)

grades[0][1] = 83
n1()

bob_grade = grades[0][1]
print("Bob's grade(New):", bob_grade)
print("New grades: ", grades)
n1()

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])




n1()