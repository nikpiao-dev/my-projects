-- The SUM() aggregate function takes a column and returns the total sum of the values in it.

SELECT SUM(plays)
FROM playlist;

-- How long is this playlist? Use SUM() to find the total duration.


-- select the table 
SELECT * 
FROM playlist;


--  find total duration
SELECT SUM(duration)
FROM playlist;