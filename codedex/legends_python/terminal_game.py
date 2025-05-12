# Checkpoint Python Project Codedex - Terminal Game

# Variables for use:
background = """
This is a Fantasy Mini-Adventure! 
You’re a wandering hero in a kingdom plagued by dark magic."""
print()

title = "Path of the Wanderer: The Journey of Rowen of Elderfall"
genre = "Fantasy Adventure"
first_name = "Rowen"
last_name = "Ashvale"
land = "Elderfall"
village = "Dunhollow"

# Introduction:
print(background)
print("Title:", title)

print()
print(first_name + " " + last_name + ", that is your name. " + "A wanderer with a quiet strength and a mysterious past.")

print()
print("The land of " + land + " awaits...")

# Player Stats:
attack = 5
block = 3
hp = 20
money = 15

# limit 3 per day, 5 hp per heal = 15 hp / day (5hp * 3/day)
heal = 5 
heals_left = 3


# Start of the adventure:
print("HP:", hp, "| Heals left:", heals_left)
print("You are in " + village + " village. The sun is rising.")
print(""" What would you do?:
      A) Visit the market
      B) Go to the forest
      C) Stay at the inn""")

choice = input("Choose from the options (A, B or C):").lower()

if choice == "a":
    print("You visit the market. A potion costs 5 coins. You have " + str(money) + " coins total.")
    potion = 5
    money -= potion
    print("Potion successfully purchased. Total coins left:", money)
elif choice == "b":
    print("You have decided to walk in the forest. But wait, a wild goblin appears!")
    print()

    enemy_hp = 10
    damage = 4

    print("Your HP:", hp, "| Enemy HP:", enemy_hp)
    print(""" Please select your next action:
        1) Attack
        2) Block
        3) Heal""")

    action = input("Choose from 1, 2, 3: ")

    if action == "1":
        enemy_hp -= attack
        print("You attack the goblin")
        print("Total enemy hp:", enemy_hp)
    elif action == "2":
        damage -= block
        if damage < 3: 
            damage = 0
        hp -= damage
        print("You blocked the attack. Goblin hits you for " + str(damage) + " damage")
    elif action == "3":
        if heals_left > 0:
            hp += heal
            if hp > 20:
                hp = 20
            heals_left -= 1
            print("You heal for 5 hp")
        else:
            print("Sorry, no heals left.")
    else:
        print("Action Invalid!")

    if enemy_hp > 0:
        hp -= damage
        print("Goblin hits you for " + str(damage) + " damage.")
        print("Your HP is now " + str(hp))

    if hp <= 0:
        print("You have been defeated by the enemy goblin. Game over.")
    else:
        print("Hurray, you have defeated the enemy goblin!")

elif choice == "c":
    print("You decided to stay at the inn. The innkeeper tells you some tales of monsters in the forest.")
else:
    print("Invalid choice.")

new_game = input("Do you want to continue? (yes / no) or (y / n): ").lower()
if new_game == "yes" or new_game == "y":
    
    # If you say "yes", a new scenario
    print("You have decided to continue your adventure.")
    print("As you walk deeper into the village, you hear rumors of a dark sorcerer living in the mountains.")
    print("""What do you do next?
            A) Investigate the rumors at the tavern.
            B) Head to the mountains to face the sorcerer.
            C) Return to the inn to rest.""")

    next_choice = input("Choose A, B, or C: ").lower()

    if next_choice == "a":
        print("You gathered information at the tavern. The locals speak of a hidden temple in the mountains.")
    elif next_choice == "b":
        print("You started your journey to the mountains. The air grows colder, and a sense of danger looms.")
    elif next_choice == "c":
        print("You returned to the inn to rest. The innkeeper warns you about the increasing darkness in the land.")
    else:
        print("Invalid choice.")

elif new_game == "no" or new_game == "n":
    print("Thanks for playing!")

else:
    print("Invalid command")
