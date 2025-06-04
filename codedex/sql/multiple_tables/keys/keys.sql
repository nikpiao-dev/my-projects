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
 
1 @sonny 13 Gold 147 918 2022
2 @jackieisonline 9 Silver 3 30 2023
3 @lilybird 7 Silver 50 101 2022
4 @intelagense 12 Gold 70 533 2022




INSERT INTO users (project_id, name, user,  user_id, likes, comments, staff_picks)
VALUES ()


-- pull up two tables:

select * from books;
select * from author;


-- Can you guess which columns are the primary keys 
-- and which one is the foreign key?

-- 