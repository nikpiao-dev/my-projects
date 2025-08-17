"""
Instructions
In the notebook on the right, we've imported pandas and created a DataFrame named movies!

Now, type the following into the input box at the bottom of the page:

movies

And press shift + enter to run the code. A table should appear.

Boom. We're now ready to learn how to use Pandas to answer questions about this data. 🙌

Bonus: Now let’s get curious. What’s a question you might ask about this dataset?

Write it as a Python comment and hit shift + enter again. For example:

# What month is the best month to release a movie? What month is the worst?
# Which film studio has the highest average profit?


"""

import pandas as pd

# Recent Oscar winners
movie_data = {
  'title': ['Parasite', 'Nomadland', 'CODA', 'Everything Everywhere All at Once', 'Oppenheimer', 'Anora'],
  'release_date': ['2019-05-30', '2020-09-11', '2021-01-28', '2022-03-11', '2023-07-21', '2024-05-24'],
  'genre': ['Thriller', 'Drama', 'Drama',  'Action', 'Biography', 'Drama'],
  'studio': ['CJ Entertainment', 'Searchlight Pictures', 'Apple TV+', 'A24', 'Universal Pictures', 'A24'],
  'budget': [11400000, 5000000, 10000000, 25000000, 100000000, 3000000],
  'box_office': [263000000, 39000000, 1900000, 143000000, 975000000, 57000000],
  'runtime_minutes': [132, 108, 111, 139, 180, 98],
  'rating': [8.5, 7.3, 8.0, 8.0, 8.6, 8.1]
}

# Create the DataFrame
movies = pd.DataFrame(movie_data)


# Print the DataFrame
print(movies)
