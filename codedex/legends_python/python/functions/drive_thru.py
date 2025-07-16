"""
Instructions
When you go to a drive-thru like McDonald's, you can order food using the item numbers. For example, a Happy Meal might be a #3!

Create a drive_thru.py program with your favorite fast food chain's menu.

Define a get_item() function that takes in one parameter, the number of the item you want to order, and returns the name of that item!

For example, if you called the function with:

Argument value 1, it could return '🍔 Cheeseburger'.
Argument value 2, it could return '🍟 Fries'.
Argument value 3, it could return '🥤 Soda'.
Argument value 4, it could return '🍦 Ice Cream'.
Argument value 5, it could return '🍪 Cookie'.
Make sure to call this function a few times to make sure that it works!

Lastly, let's do the following:

Create a welcome menu and put that in a welcome() function.
Create a main program that takes in user input with input().

"""



def get_item(num):
    if num == 1:
        return '🍔 Cheeseburger'
    elif num == 2:
        return '🍟 Fries'
    elif num == 3:
        return '🥤 Soda'
    elif num == 4:
        return '🍦 Ice Cream'
    elif num == 5:
        return '🍪 Cookie'
    else:
        return 'Invalid item number'


def welcome():
    menu = """
    McValue Menu:

    1. 🍔 Cheeseburger
    2. 🍟 Fries
    3. 🥤 Soda
    4. 🍦 Ice Cream
    5. 🍪 Cookie
    """
    print("Welcome to McDonald's! We're happy to serve you. 🍟🍔")
    return menu

print(welcome())
choice = int(input("What would you like to order?: "))

print(get_item(choice))

