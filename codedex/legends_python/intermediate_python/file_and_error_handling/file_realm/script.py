"""

Instructions
✨ Here at Codédex, we are 🤩 big fans of music 🎹. The only thing better than a perfect playlist is a playlist with all your favorite songs. Let's create a Python script that organizes the songs into a .txt file. Let's make a playlist!

First, let's define a dictionary to store liked songs:

liked_songs = {
  'title': 'artist'
}

Next, create a function to display and write liked songs to a file:

def write_liked_songs_to_file(liked_songs, file_name):

Open the file in write mode.
Write each song and artist by iterating through the liked_songs dictionary.
Your liked_songs.txt file should look something like this:

Liked Songs:
Bad Habits by Ed Sheeran
I'm Just Ken by Ryan Gosling
Mastermind by Taylor Swift
Uptown Funk by Mark Ronson ft. Bruno Mars
Ghost by Justin Bieber

"""


liked_songs = {
    'Blinding Lights': 'The Weeknd',
    'Shivers': 'Ed Sheeran',
    'Levitating': 'Dua Lipa',
    'As It Was': 'Harry Styles',
    'Good 4 U': 'Olivia Rodrigo'
}

def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as file:
        file.write('Liked Songs:\n')
        for title, artist in liked_songs.items():
            file.write(f'{title} by {artist}\n')
    print(f'Liked songs has been added to {file_name}\n')

write_liked_songs_to_file(liked_songs, 'liked_songs.txt')

with open('liked_songs.txt', 'r') as file:
    content = file.read()
    print(content)

