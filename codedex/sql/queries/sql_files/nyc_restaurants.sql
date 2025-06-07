--  Instructions:

-- It’s in a restaurants table that you can access:
SELECT *
FROM restaurants;

-- It has the following columns:

-- id
-- name
-- cuisine
-- borough
-- neighborhood
-- price
-- yelp_review

-- Play around with the table and try to find out:

-- What are all the unique cuisines in the table?
  SELECT DISTINCT cuisine
  FROM restaurants;

-- What are all the Chinese restaurants? Italian?
  SELECT *
  FROM restaurants
  WHERE cuisine = "Chinese" OR cuisine = "Italian";

  SELECT * 
  FROM restaurants 
  WHERE cuisine LIKE "Chinese"
    OR cuisine LIKE "Italian";

  SELECT * 
  FROM restaurants 
  WHERE cuisine LIKE "%Chinese%" 
   OR cuisine LIKE "%Italian%";


-- What are all the spots in Greenpoint 
-- (a neighborhood in Brooklyn)?

    SELECT *
    FROM restaurants
    WHERE neighborhood LIKE "%Greenpoint%";

    SELECT *
    FROM restaurants
    WHERE neighborhood LIKE "Greenpoint";


-- Where are the cheap eats? The bougie ones?
    
  SELECT *
  FROM restaurants
  WHERE price = '$';

  SELECT *
  FROM restaurants
  WHERE price LIKE "$$$";
