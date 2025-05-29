#Boolean Expressions and Relational Operators

def n1(): #new line
    print('\n')

n1()


#Boolean Expressions (True or False)

bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3 * 3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1), type(bool2), type(bool3), type(bool4))

bool5 = "True"
print(type(bool5))


n1()

#Relational and Boolean Operators

greater_than = 7 > 5
less_than = 5 < 7

greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7
equals = 7 == 7
not_equals = 7 != 8

test_and = (7 > 5) and (5 < 7) # TRUE
test_and2 = (7 > 5) and (5 < 7) # FALSE
test_or = (7 > 5) or (5 < 7) # TRUE
test_or2 = (7 > 5) or (5 > 7) # TRUE
test_not  = not True # FALSE

n1()

#Conditional Statements - if/else

def drink(money):
    if money >= 2:
        return "You got yourself a drink!"
    else:
        return "No drink for you!"
    
print(drink(3))
print(drink(1))


# def alcohol(age, money):  # Refactored version
#     if age >= 21:
#         if money >= 5:
#             return "We're getting a drink!"
#         else:
#             return "Come back with more money."
#     else:
#         if money >= 5:
#             return "Nice try, kid!"
#         else:
#             return "You're too young and broke."


# Parenthesis in conditionals help with readability
def alcohol(age, money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money."
    elif (age < 21) and (money >= 5):
        return "Nice try, kid!"
    else:
        return "You're too young and broke."
    

print(alcohol(21, 5))
print(alcohol(21, 4))
print(alcohol(20, 5))
print(alcohol(20, 4))

