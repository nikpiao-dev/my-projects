Instructions:

-- Let’s try it out using the two tables in the database again: books and authors.

-- Join the two tables using LEFT JOIN/LEFT OUTER JOIN and select 2-3 columns of your choice.

-- Do you notice the difference?


-- EXAMPLE:
SELECT columns
FROM table1
LEFT JOIN table2
  ON table1.column1 = table2.column2;



-- select both tables
select * 
from books 
limit 5;

select * 
from authors 
limit 5;


-- Use left join to combine both tables