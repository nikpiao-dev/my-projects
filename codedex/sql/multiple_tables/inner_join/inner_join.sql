-- We have two tables in the database: books and authors.

-- Check them out again to see how they could be connected.

-- Join the two tables using JOIN/INNER JOIN and select 2-3 columns of your choice.

-- select both tables
SELECT *
FROM books
LIMIT 5;

SELECT *
FROM authors
LIMIT 5;


-- use JOIN or INNER JOIN to combine:

-- example: 
SELECT columns
FROM table1
INNER JOIN table2
  ON table1.column1 = table2.column2;


-- use JOIN or INNER JOIN to combine:

SELECT name, title, year, books 
FROM books
INNER JOIN authors
    ON  books.author_id = authors.id;


SELECT title, name, year, born, books
FROM books
JOIN authors
    ON books.author_id = authors.id;