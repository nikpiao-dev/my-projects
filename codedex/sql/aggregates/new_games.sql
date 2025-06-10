-- Instructions:

-- It’s in a new games table that you can play around with:
SELECT *
FROM games;

-- It has the following columns:

-- id
-- title
-- genre
-- studio
-- headquarters
-- language
-- year
-- metascore
-- players


-- What is the most popular game in the list?

  SELECT title, MAX(players)
  FROM games

-- What are the counts of all the programming languages?

  SELECT COUNT(language)
  FROM games;

-- What are the average Metascores for each of the genres?

  SELECT title, genre, AVG(metascore)
  FROM games
  GROUP BY genre;