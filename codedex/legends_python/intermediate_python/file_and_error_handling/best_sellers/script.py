"""

Instructions
We've all seen, perhaps bought, one of our favorite products with a "Bestseller" sticker. 🏅

Let’s write a program to read a CSV file and find the best-selling book of all time. 🔍

Download this CSV file of all-time bestselling books data!
Open the Bestseller - Sheet1.csv file in "read" mode.
Use the CSV reader to navigate through the data and find the book with the highest sales, via the sales in millions column.
Create a new file called bestseller_info.csv with the CSV writer.
In the new file, use .writerow() to add new CSV data.
Up next, let’s learn about what to do in the face of the unexpected, we'll be exploring error handling.


# example csv

import csv

# Open the CSV file in 'read' mode
with open('example.csv', 'r') as file:
  # Create a CSV reader object
  csv_reader = csv.reader(file)

  for row in csv_reader:
    print(row)

"""


import csv

# Open the CSV file in 'read' mode
with open('Bestseller_Sheet.csv', 'r') as file:
  # Create a CSV reader object
  csv_reader = csv.reader(file)

  for row in csv_reader:
    print(row)
