-- # AVG()

-- Use the AVG() function to calculate the average value of a column.

SELECT AVG(plays)
FROM playlist;


-- In 1998, the average length of a song on Billboard Hot 100 was 4 minutes and 22 seconds. In 2018, the average length was approximately 3 minutes and 30 seconds.

-- How long is an average song? Find the average duration of a song. ⏰


SELECT AVG(duration)
FROM playlist;