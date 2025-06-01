-- Find all the shows in the table that bombed (with a tomatometer less than 60).

-- 🍅 When at least 60% of reviews for a movie or TV show are positive, a red tomato is displayed to indicate it's "Fresh".

-- 🦠 When less than 60% of reviews for a movie or TV show are positive, a green splat is displayed to indicate it's "Rotten".


-- SELECT * FROM shows;

SELECT *
FROM shows
WHERE tomatometer < 60;
