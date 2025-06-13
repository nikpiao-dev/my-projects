import sqlite3

# connect to database
conn = sqlite3.connect('petstore.db')

# CREATE cursor to interact w/ db
cursor = conn.cursor()

# CREATE TABLE
cursor.execute('''
CREATE TABLE IF NOT EXISTS pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    species TEXT,
    age INTEGER
)
''')

# Insert single pet
cursor.execute("INSERT INTO pets (name, species, age) VALUES (?, ?, ?)", ("John", "cat", 4))


# List of pets
pets = [
    (3, 'Mochi', 'cat', 1), 
    (4, 'Prince Harry', 'cat', 1),
    (5, 'Cloud', 'cat', 0),
    (6, 'Max', 'cat', 2)
]


# Insert each pet into the table (w/o using "executemany")
for pet in pets:
    cursor.execute("INSERT INTO pets (name, species, age) VALUES (?, ?, ?)", pet)

# Commit changes to save them
conn.commit()

# Retrieve and print rows for confirmation
cursor.execute("SELECT * FROM pets")
rows = cursor.fetchall()
for row in rows:
    print(row)


# Close the connection
conn.close()


