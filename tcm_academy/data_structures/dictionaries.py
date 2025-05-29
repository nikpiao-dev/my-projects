# New line function
def n1():
    print('\n')


# Dictionaries - key/value pairs {}


drinks = {"White Russian": 8, "Old Fashioned": 12, "Lemon Drop": 5}
# drink is the (key), prices is the (value)
print(drinks)

n1()

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": [
    "Gene", "Luis", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print("Original Dict:", employees)
n1()

employees['Legal'] = ["Mr. Frond"] # Add a new key/value pair
print("New Dict:", employees)
n1()

employees.update({"Sales": ["Andy", "Ollie"]}) # add a new key/value pair
print("Updated Dict:", employees)
n1()

print("Original drinks:", drinks)
drinks['White Russian'] = 9 # modify dictionary
print("Updated drinks:", drinks)

print(drinks.get('White Russian'))







































n1()
