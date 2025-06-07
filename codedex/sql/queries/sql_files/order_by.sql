-- The ORDER BY statement sorts rows of data in ascending or descending order. 
-- By default, this command sorts the data in ascending order.

SELECT name, genre, stream, year
FROM shows
ORDER BY year;

-- This results into selecting 4 columns from our table but if you look closely, the year column is sorted into ascending order.

name	             genre 	       stream	     year
Sex and the City	 Drama	       HBO	         1998
The Sopranos	     Crime,Drama   HBO	         1999
One Piece	         Anime	       Crunchyroll	 1999
Bleach	             Anime	       Crunchyroll	 2004



-- Let’s say we want to get all the latest shows this time, 
-- we will have to sort the year column into descending order using the DESC command:
SELECT name, genre, stream, year
FROM shows
ORDER BY year DESC;




-- Instructions:
-- Using ORDER BY, sort the table from the highest tomatometer rating to lowest.


SELECT name, genre, stream, tomatometer
FROM shows
ORDER BY tomatometer DESC;

