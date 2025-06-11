-- # UPDATE
-- Mistakes and outdated data happen, which means we need to go in and update some values in the table.

-- The UPDATE statement edits a row in a table.

-- Elon Musk changed Twitter’s name to X in 2023, let’s update the name:

-- UPDATE companies
-- SET name = 'X'
-- WHERE name = 'Twitter';

-- Here, we are updating the row where name = 'Twitter' and changing the name to 'X' instead.

-- We can also use WHERE for a different column:

-- UPDATE companies
-- SET headquarters = 'Brooklyn 🌉'
-- WHERE id = 4;

-- Here, we are updating the row where id = 4 and changing the headquarters to Brooklyn 🌉.



-- Instructions:
-- update all websites in the websites column.

-- It should look something like:

-- id	name	headquarters	year	website
-- 1	X	San Francisco 🌁	2006	x.com
-- 2	Duolingo	Pittsburgh 🐝	2011	duolingo.com
-- 3	BeReal	Paris 🇫🇷	2020	bereal.com
-- 4	Codédex	Brooklyn 🌉	2022	codedex.io


-- Use SELECT * to make sure it’s good to go!




CREATE TABLE companies (
  id INTEGER,
  name TEXT,
  headquarters TEXT,
  year INTEGER
);

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


select * from companies;