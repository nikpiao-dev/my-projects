-- The BETWEEN operator is used in a WHERE clause to 
-- filter the result set within a certain range. 
-- The range must be separated by an AND keyword.

-- For example, this query filters the result to only include shows 
-- between the years 2020 and 2025 (inclusive):

SELECT *
FROM shows
WHERE year
BETWEEN 2020 AND 2025;


-- In this statement, BETWEEN filters the result to only include shows with names that begin with the letter 'A' up to 'D':

SELECT *
FROM shows
WHERE name
BETWEEN 'A' AND 'D';


-- Note: BETWEEN stops at the second letter, but doesn’t include values that begin with the second letter.



-- Instructions:

The New Golden Age of Television is considered to have begun in 1999 with Jersey mobster show, “The Sopranos”.

-- Find all shows released in the Golden Age, from 1999 to 2024. Have you seen any of those?