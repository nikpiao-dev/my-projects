-- Insert into

-- create table 'companies'

CREATE TABLE companies (
  id INTEGER,
  name TEXT,
  headquarters TEXT,
  year INTEGER
);

-- Insert values into newly created table

INSERT INTO companies (id, name, headquarters, year)
VALUES (1, 'Twitter', 'San Francisco 🌁', 2006);

INSERT INTO companies (id, name, headquarters, year)
VALUES (2, 'Duolingo', 'Pittsburgh 🐝', 2011);

INSERT INTO companies (id, name, headquarters, year)
VALUES (3, 'BeReal', 'Paris 🇫🇷', 2020);

INSERT INTO companies (id, name, headquarters, year)
VALUES (4, 'Codedex', 'New York 🗽', 2022);


-- Find 2-3 tech companies that you like 
-- and use INSERT statements to add their info (id, name, headquarters, founded year) into the companies table you created.



INSERT INTO companies (id, name, headquarters, year)
VALUES 
(5, 'Google', 'Mountain View, USA', 1998),
(6, 'Microsoft', 'Redmond, USA', 1975),
(7, 'Amazon', 'Seattle, USA', 1994);


-- Try SELECT * after.
select * from companies;