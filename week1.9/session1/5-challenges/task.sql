.headers on
.mode column

-- Write your sql for each task here - you can use comment (start with --) to add notes or number them. Remember your ; at the end of each query!
-- with multiple queries in the file, sql will run then one after the other and print them all out, so I recommend testing after each one.

-- bronze
SELECT * FROM drivers

SELECT name, price FROM menu_items
WHERE restaurant_id = 3;

SELECT name FROM restaurants
WHERE cuisine = 'Indian';

select count(*) FROM customers


-- silver
SELECT name FROM restaurants
WHERE postcode glob 'LS6*'

-- gold
SELECT customers.name as 'customer name', customers.customer_id, restaurants.name as 'restaurant name', restaurants.restaurant_id, orders.order_time FROM orders, customers, restaurants 
WHERE orders.restaurant_id = restaurants.restaurant_id
AND orders.customer_id = customers.customer_id
AND orders.status = 'placed'