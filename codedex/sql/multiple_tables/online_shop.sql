-- Instructions:

-- Imagine you run an online Shopify store and have to manage all the orders, products, and customers.

-- screenshot

-- The data are all kept in three tables.

-- orders has the following columns:

-- id
-- date
-- customer
-- customer_id
-- fulfilled
-- item_id
-- products has the following columns:

-- id
-- name
-- price
-- active
-- inventory
-- customers has the following columns:

-- id
-- name
-- location
-- email_subscriber
-- Use joins and what we learned in previous chapters to find insights about the data. You can formulate your own questions, but here are some of ours:

-- What are the best selling items? What are the most underperforming ones?
-- What are all the orders the customers bought?
-- What days had the highest sales? And the lowest?


-- select both tables to check info
select *
from orders
limit 5;

select *
from products
limit 5;

select * 
from customers
limit 5;


-- Questions:


-- What are the best selling items? What are the most underperforming ones?


-- What are all the orders the customers bought?


-- What days had the highest sales? And the lowest?