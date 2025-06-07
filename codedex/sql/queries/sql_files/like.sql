--  LIKE operator can be used to search for a pattern in a column
-- It’s used in the WHERE clause:

SELECT * 
FROM shows 
WHERE name LIKE 'T%';

-- This statement filters the result to only include shows with names that begin with the letter 'T'.

-- The percentage sign % is a wildcard character that can be used with LIKE.


-- The % can be used in different ways:

A% matches values that begin with letter 'A'.
%z matches values that end with 'z'.


-- Can also use % both before ad after a pattern:
SELECT * 
FROM shows 
WHERE name LIKE '%the%';



-- Instruction:
-- Select all the shows with the genre
-- including pattern "com" for genres like sitcom, rom-com, stand-up comedy, etc.

SELECT *
FROM shows
WHERE genre LIKE '%com%';