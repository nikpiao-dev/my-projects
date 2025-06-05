Instructions:

-- Let’s try it out using the two tables in the database again: books and authors.

-- Join the two tables using LEFT JOIN/LEFT OUTER JOIN and select 2-3 columns of your choice.

-- Do you notice the difference?


-- EXAMPLE:
SELECT columns
FROM table1
LEFT JOIN table2
  ON table1.column1 = table2.column2;

-- Using Inner Join
SELECT name, year, country
FROM directors
INNER JOIN movies
  ON directors.name = movies.director;


-- NOTES: So what’s the difference between JOIN and LEFT JOIN?

JOIN:

-- Returns rows where there’s a match in both tables.
-- If there’s no match, that row is excluded.

LEFT JOIN:

-- Returns all rows from the left table, and matched rows from the right.
-- If there’s no match on the right, you’ll still get the left row... but with NULLs for the right-side columns.



-- select both tables
select * 
from books 
limit 5;

select * 
from authors 
limit 5;


-- Use left join to combine both tables
