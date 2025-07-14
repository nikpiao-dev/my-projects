"""
Instructions
Let's try a classic Computer Science project: simple calculator program! 🔢

Create a calculator.py program and define these five functions:

add(a, b) that adds two numbers a and b.
subtract(a, b) that subtracts two numbers a and b
multiply(a, b) that multiplies two numbers a and b.
divide(a, b) that divides two numbers a and b.
exp(a, b) that takes a to the exponent (or power) of b.
Make sure to return the result in each function definition.

Test your calculator by calling each function once to make sure that it works!

"""


def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply( x, y):
  return x * y

def divide(x, y):
  return x / y

def exp(x, y):
  return x ** y

print(add(1, 2))
print(subtract(3, 4))
print(multiply(5, 6))
print(divide(7, 8))
print(exp(9, 10))

print(add(3, 5))
print(subtract(7, 2))
print(multiply(4, 8))
print(divide(9, 3))
print(exp(2, 3))
