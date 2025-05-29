""" 
# Introduction to Functions 
    - Reusable block of code (like a program)

### def keyword,function name, parenthesis and colon, 
### parameters, return statement, function call

# def greeting(parameter):
    return statement

greeting()
"""

age = 35 #global variable
birthday = 1

age += birthday
print(age)

# def who_am_i():
#     name = "Heather" #local variable
#     age = 32
#     print(f"My name is {name} and I am {age} years old.") #f-string
#who_am_i()

def who_am_i(name, age):
    print(f"My name is {name} and I am {age} years old.") #f-string

who_am_i("Heath", 32)

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

def subtract(x,y):
    print(x - y)

subtract(6, 5)

def multiply(x,y):
    return x * y

print(multiply(5, 4))

result1 = multiply(4, 2)
result2 = multiply(3, 6)
print(result1 + result2)


def square_root(x): #square_root
    print(x ** .5)

square_root(64)

def n1(): #new line
    print('\n')

n1()