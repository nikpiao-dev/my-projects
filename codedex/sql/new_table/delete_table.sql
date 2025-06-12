-- # DELETE FROM
-- DELETE FROM statement removes one or more rows from a table.

-- Since BeReal got acquired in 2024, we can delete it from the companies table with:

-- DELETE FROM companies
-- WHERE name = 'BeReal';

-- Here, we are deleting the whole row(s) WHERE name = 'BeReal';



-- Instructions:

-- Delete one or two rows in your table.

-- Use SELECT * to query everything again to make sure it’s good to go!


-- Write code below 💖



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

DELETE FROM companies
WHERE name = 'BeReal';


select * from companies;