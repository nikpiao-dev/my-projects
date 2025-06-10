-- The GROUP BY statement groups rows of data with the same values into buckets. It’s often used with aggregate functions to group the result by one or more columns.

SELECT genre, COUNT(*) 
FROM playlist 
GROUP BY genre;



-- Suppose we want to see the average song lengths for each genre, we can do:
SELECT genre, AVG(duration)
FROM playlist 
GROUP BY genre;




-- Using GROUP BY, find all the different artists and their average number of plays in two columns.


SELECT * 
FROM playlist;

SELECT artist, AVG(plays)
FROM playlist
GROUP BY artist;