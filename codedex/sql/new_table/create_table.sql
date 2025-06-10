-- CREATE TABLE statement creates a brand new table in a database.

-- Example) we are creating a new table called companies:
CREATE TABLE companies (
  id INTEGER,
  name TEXT,
  headquarters TEXT,
  year INTEGER
);

-- Here, we are creating a new table of companies with the following columns:

-- id column of the data type INTEGER.
-- name column of the data type TEXT.
-- headquarters column of the data type TEXT.
-- year column of the data type INTEGER.


-- -- DATA Types:
-- All the data stored in a database has a type. The data type lets the database know what to expect from each column and determines the kind of interactions that can happen.

-- Some of the most common data types are:

-- TEXT: a text string
-- INTEGER: a positive or negative whole number
-- REAL: a positive or negative decimal number
-- DATE: a date format (YYYY-MM-DD)


-- Instructions:

CREATE TABLE companies (
  id INTEGER,
  name TEXT,
  headquarters TEXT,
  year INTEGER
);

SELECT *
FROM companies;


INSERT INTO companies (id, name, headquarters, year)
VALUES (1, 'Twitter', 'San Francisco 🌁', 2006);

INSERT INTO companies (id, name, headquarters, year)
VALUES (2, 'Duolingo', 'Pittsburgh 🐝', 2011);

INSERT INTO companies (id, name, headquarters, year)
VALUES (3, 'BeReal', 'Paris 🇫🇷', 2020);

INSERT INTO companies (id, name, headquarters, year)
VALUES (4, 'Codedex', 'New York 🗽', 2022);

ALTER TABLE companies
ADD COLUMN website TEXT;

UPDATE companies
SET name = 'X'
WHERE name = 'Twitter';

UPDATE companies
SET headquarters = 'Brooklyn 🌉'
WHERE id = 4;

UPDATE companies
SET website  = 'x.com'
WHERE id = 1

UPDATE companies
SET website = 'duolingo.com'
WHERE id = 2

UPDATE companies
SET website = 'bereal.com'
WHERE id = 3

UPDATE companies
SET website = 'codedex.com'
WHERE id = 4

DELETE FROM companies
WHERE name = 'BeReal';
