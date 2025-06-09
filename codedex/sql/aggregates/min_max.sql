-- MIN() and MAX() are exactly how they sound: they return the minimum and maximum value in a column, respectively.


--  this returns the smallest value in the plays column:
SELECT MIN(plays)
FROM playlist;


--  finds the most popular song in the table:

SELECT title, artist, MAX(plays)
FROM playlist;


-- What is the oldest song in the playlist? What about the newest song?

SELECT *
FROM playlist;

SELECT title, artist, MIN(year)
FROM playlist;

SELECT title, artist, MAX(year)
FROM playlist;