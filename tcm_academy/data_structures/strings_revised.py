# Strings Revisited

def n1(): # function for a new line
    print('\n')
n1()


# Advance strings

my_name = "Thompson"
print(my_name[0])  # first letter
print(my_name[-1]) # last letter


sentence = "This is a sentence."
print(sentence[0:4]) # "This"
print(sentence[:4]) # "This"
print(sentence[0:3 + 1]) # "This"


print(sentence.split()) # delimiter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)


print(sentence_split) # returns as a list
print(sentence_join) # joined with spaces,; returns as a string


print(type(sentence_split))
print(type(sentence_join))

ip_address = "192.168.138.1"
print("IP address:", ip_address)
print(ip_address.split('.'))

ip_address_split = ip_address.split('.')
ip_address_join  = '.'.join(ip_address_split)

print(ip_address_split)
print(ip_address_join)


n1()

quote = "He said, 'give me all your money'"
quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                        hello            "
print(too_much_space.strip()) # default is space


print("A" in "Apple") # return True
print("a" in "Apple") # return False - case sensitive

letter = "A"
word = "Apple"
print(letter.lower() in  word.lower()) # improved

print("b".upper() in "Baltimore")
print("b" in "Baltimore".lower())
n1()

# user_input = input("Enter yes or no: ")
# if user_input.lower().strip() == "yes":
#     print("You agree!")
# else:
#     print("You disagree!")

movie = "The Hangover"
print("My favorite movie is {}.".format(movie)) # format option
print("My favorite movie is %s." % movie) # percent option
print(f"My favorite movie is {movie}.") # f-strings option 

