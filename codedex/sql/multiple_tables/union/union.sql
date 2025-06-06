-- Instructions:

-- We have a students table and a teachers table in a school database ready for you.
-- Use SELECT to see what they look like.
-- Let's do a roll call. Can you use UNION to get all the names from both tables?



-- Example:
SELECT name
FROM directors
UNION
SELECT name
FROM movies;

-- select both tables to check data:
select * 
from students 
limit 5;

select * 
from teachers 
limit 5;



-- USE union operator to combine two tables into one list w/o duplicates:

SELECT name 
FROM students
UNION
SELECT name
FROM teachers;