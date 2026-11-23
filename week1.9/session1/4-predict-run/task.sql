.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- A

SELECT name FROM restaurants
WHERE hygiene_rating = 5;

-- B

SELECT name FROM restaurants
WHERE postcode LIKE 'LS6%';

-- C

SELECT name FROM restaurants
WHERE cuisine = 'italian';

-- D

SELECT name FROM restaurants
WHERE cuisine = 'Italian' OR cuisine = 'Thai' AND hygiene_rating = 5;