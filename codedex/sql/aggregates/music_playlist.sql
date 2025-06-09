-- # Introduction

-- Aggregate functions are used to perform calculations and return a single value.

-- The most common aggregate functions are:

-- COUNT(): returns the number of rows.
-- MAX(): returns the largest value in a column.
-- MIN(): returns the smallest value in a column.
-- SUM(): returns the total sum in a column.
-- AVG(): returns the average value in a column.

-- Aggregate functions are used a ton with something called a GROUP BY which we will also learn later in this chapter.



SELECT *
FROM playlist;

-- It has the following columns:

-- title
-- artist
-- album
-- year
-- genre
-- plays (total number of streams)
-- duration (song length in seconds)