-- Create a users table and a projects table:

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    level INT,
    rank VARCHAR(20),
    following INT DEFAULT 0,
    followers INT DEFAULT 0,
    signed_up DATE
);

CREATE TABLE projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    username VARCHAR(50),
    user_id INT, -- (foreign key)
    likes INT DEFAULT 0,
    comments INT DEFAULT 0,
    staff_picks BOOLEAN DEFAULT FALSE,
);


-- Insert multiple users
INSERT INTO users (id, username, level, rank, following, followers, signed_up)
VALUES 
(1, '@sonny', 13, 'Gold', 147, 918, '2022'),
(2, '@jackieisonline', 9, 'Silver', 3, 30, '2023'),
(3, '@lilybird', 7, 'Silver', 50, 101, '2022'),
(4, '@intelagense', 12, 'Gold', 70, 533, '2022');
 

-- Insert multiple projects into the 'projects' table
INSERT INTO projects (project_id, name, username, user_id, likes, comments, staff_picks)
VALUES
(1001, 'Karaoke Nite', '@sonny', 1, 21, 6, TRUE),
(1002, 'Welp', '@sonny', 1, 13, 1, TRUE),
(1003, '7 Minutes in Heaven', '@jackieisonline', 2, 15, 3, TRUE),
(1004, 'Chao Bing', '@jackieisonline', 2, 13, 4, TRUE),
(1005, 'ifeelsomuchsha.me', '@jackieisonline', 2, 19, 6, TRUE),
(1006, 'Wobble Digging Robot', '@intelagense', 4, 15, 6, TRUE),
(1007, 'Songbird Sketchbook', '@lilybird', 3, 25, 7, TRUE);




-- Note: The projects table can also have its own primary key (maybe project_id). 
-- And it can have other foreign keys that link out to other primary keys in other tables (i.e. posts table, courses table).


--Instructions:


-- pull up two tables:

select * from books;
select * from author;


-- Can you guess which columns are the primary keys 
-- and which one is the foreign key?

-- 