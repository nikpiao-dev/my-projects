"""
Instructions
The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin


Write a program that asks the user some questions with the int() and input() functions:

Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk

If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
Else, output the message "Wrong input."
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold

If the answer is 1, Hufflepuff +2.
Else if answer is 2, Slytherin +2.
Else if answer is 3, Ravenclaw +2.
Else if answer is 4, Gryffindor +2.
Else, output the message "Wrong input."
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum

If the answer is 1, Slytherin +4.
Else if the answer is 2, Hufflepuff +4.
Else if the answer is 3, Ravenclaw +4.
Else if the answer is 4, Gryffindor +4.
Else, output "Wrong input."
Lastly, print out the score for each house.

Bonus: If you want to go further, see if you can figure out how to print out the house with the most points!
"""
# 💖 Hogwarts House Quiz

# 🦁 Gryffindor
# 🦅 Ravenclaw
# 🦡 Hufflepuff
# 🐍 Slytherin

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

answer = int(input("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n"))
if answer == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif answer == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong Input")

answer = int(input("""\nQ2) When I'm dead, I want people to remember me as:
1) The Good
2) The Great
3) The Wise
4) The Bold
"""))
if answer == 1:
  Hufflepuff += 2
elif answer == 2:
  Slytherin += 1
elif answer == 3:
  Ravenclaw += 1
elif answer == 4:
  Gryffindor += 1
else:
  print("Wrong Input")

answer = int(input("""\nQ3) Which kind of instrument most pleases your ear?
1) The violin
2) The trumpet
3) The piano
4) The drum
"""))
if answer == 1:
  Slytherin += 1
elif answer == 2:
  Hufflepuff += 2
elif answer == 3:
  Ravenclaw += 1
elif answer == 4:
  Gryffindor += 1
else:
  print("Wrong Input")

# Determine the house with the highest score
max_points = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)

print("\nYour Hogwarts House is:")
if Gryffindor == max_points:
  print("🦁 Gryffindor!")
elif Ravenclaw == max_points:
  print("🦅 Ravenclaw!")
elif Hufflepuff == max_points:
  print("🦡 Hufflepuff!")
else:
  print("🐍 Slytherin!")

