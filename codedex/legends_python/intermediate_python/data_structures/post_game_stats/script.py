"""

Instructions:

Imagine you have a dataset 📊 with information about your favorite sports team. 🏀🎾⚽ The goal is to use Python's data structures to organize and analyze this data.

If you can't think of any, feel free to use the 🏈 Super Bowl 2024 champions, the Kansas City Chiefs. 🏆

As a data analyst for the Kansas City Chiefs you have been given a dataset containing information about the players, their positions, and some game statistics.

Let's start analyzing!

Create a list of dictionaries where each dictionary represents a player. Include attributes such as 'name,' 'position,' and 'jersey number.'
Print out a list of all player positions in the dataset.
Choose a player and update their game statistics in the dataset.
Calculate the average statistics (e.g., yards gained, touchdowns) for all players and print the results.
Congratulations for reaching the end of this chapter! Using data structures, you were able to organize and analyze data for the Chiefs. 😎 Think of all the things you can analyze!

✨ Just remember practice makes perfect. ✨

"""

# Players stats:


players_info = [
  {
    "name": "LeBron James",
    "position": "Forward",
    "jersey number": 23,
    "team": "Los Angeles Lakers",
    "points_per_game": 28.1,
    "assists_per_game": 7.4,
    "rebounds_per_game": 8.2,
    "steals_per_game": 1.3
  },
  {
    "name": "Stephen Curry",
    "position": "Guard",
    "jersey number": 30,
    "team": "Golden State Warriors",
    "points_per_game": 27.3,
    "assists_per_game": 6.4,
    "rebounds_per_game": 5.1,
    "steals_per_game": 1.2
  },
  {
    "name": "Nikola Jokić",
    "position": "Center",
    "jersey number": 15,
    "team": "Denver Nuggets",
    "points_per_game": 26.5,
    "assists_per_game": 9.0,
    "rebounds_per_game": 12.3,
    "steals_per_game": 1.4
  },
]

# Print players position
print("Player Positions:\n")

for player in players_info:
  print(f"{player['position']} - {player['name']}")

print('\n')

# Update player game statistics

players_info[1]["points_per_game"] = 29.2

for player in players_info:
  if player['name'] == 'Nikola Jokić':
    player['points_per_game'] = 27.5
    player['assists_per_game'] = 10.3
    player['rebounds_per_game'] = 12.8

print("Player info:\n", players_info[1], '\n')
print("Player info:\n", players_info[2], '\n')

# Calculate average statistics

total_points = 0
total_assists = 0
total_rebounds = 0
total_steals = 0
num_players = len(players_info)

for player in players_info:
  total_points += player["points_per_game"]
  total_points += player["rebounds_per_game"]
  total_points += player["assists_per_game"]
  total_points += player["steals_per_game"]

avg_points = total_points / num_players
avg_rebounds = total_points / num_players
avg_assists = total_points / num_players
avg_steals = total_points / num_players

print('\n Average Statistics:\n')

print(f"Average Points Per Game: {avg_points}")
print(f"Average Rebounds Per Game: {avg_rebounds}")
print(f"Average Assists Per Game: {avg_assists}")
print(f"Average Steals Per Game: {avg_steals}")

