-- Bff
-- Codedex

-- Here’s a recap:

-- CREATE TABLE adds a new table.
-- INSERT INTO adds a new row.
-- ALTER TABLE/ADD COLUMN adds a new column.
-- UPDATE/SET updates a row.
-- DELETE FROM deletes a row(s).

-- Instructions:
-- It’s 2024 and it’s so hard to keep track of all your friend’s birthdays and contact info!

-- Make a personal relationship management tool (sometimes nicknamed “personal CRM”), that helps people organize and manage their personal and professional relationships!

-- Start by using a CREATE TABLE and add a few columns.

-- Here are some ideas:

-- name
-- birthday
-- location
-- note
-- anything else that’s not sensitive info!
-- And fill it in with their details!

-- Now, you can always text them on their birthday!

CREATE TABLE bffs (
  name TEXT,
  birthday TEXT,
  location TEXT,
  note TEXT
);


INSERT INTO bffs (id, name, birthday, location, note) VALUES
('Ava Moon', '1995-04-21', 'Seattle, WA', 'Loves photography and hiking.'),
('Liam Chen', '1993-09-10', 'Austin, TX', 'Met during coding bootcamp.'),
('Sofia Reyes', '1997-01-15', 'Miami, FL', 'Always brings snacks to study sessions.'),
('Noah Patel', '1994-12-05', 'Chicago, IL', 'Big fan of sci-fi movies and trivia nights.');


SELECT * FROM bffs;