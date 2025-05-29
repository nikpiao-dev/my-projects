"""
    Programming 101 - academy.tcm
"""


# Part 1 - Strings

print("Hello, World")
print('Hello World!')
print('\n') # new line

# Math - Arithmetic Operations

print(50 + 50) #add
print(52 - 4) #subtract
print(52 * 3) #multiply
print(50 / 5) #divide
print(50 + 50 - 50 * 50 / 50) #P E M D A S
print(50 ** 2) #exponents
print(50 / 6) #division with a remainder
print(50 % 6) #modulo - takes what is left over
print(50 // 6) #no remainder


#Variables and Basic Methods
age = 35 #integer
print("Before:", age)

age = 36
print("After:", age) #variables are mutable (can be change)

name = "Health" #string
gpa = 3.5 #float

print(name)
print(gpa)
print(int(35.9)) #will it round? No!

quote = "All is fair in love and war."
print(quote)

print(quote.upper()) #uppercase 
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #count characters

#concatenation 
print('My name is ' + name + ' and I am ' + str(age) + ' years old.')

age += 1
birthday = 1

age += birthday
print(age)

#User Input - always return user's input as string (default)

x = input('Give me a number: ')
y = input('Give me another number: ')


# x, y = int(x), int(y)
# print(x + y)

# print(int(x) + int(y))

# x = int(input('Give me a number: '))
# y = int(input('Give me another number: '))

print(x + y)

