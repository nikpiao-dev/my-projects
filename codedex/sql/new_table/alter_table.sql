-- # ALTER TABLE
-- So what happens when we want to add a new column to a table?

-- ALTER TABLE/ADD COLUMN statement adds a new column to an existing table.

-- ALTER TABLE companies
-- ADD COLUMN about TEXT;

-- This statement adds a new TEXT column called about to the companies table.

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

INSERT INTO companies (id, name, headquarters, year)
VALUES 
(5, 'Google', 'Mountain View, USA', 1998),
(6, 'Microsoft', 'Redmond, USA', 1975),
(7, 'Amazon', 'Seattle, USA', 1994);


-- In the code editor, add a website column to the companies table.

ALTER TABLE companies
ADD COLUMN website TEXT;

select * from companies;