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


-- What are the best selling items? 

SELECT products.name, COUNT(*) AS total_orders
FROM orders
JOIN products ON orders.item_id = products.id
GROUP BY products.name
ORDER BY total_orders DESC;


-- What are the most underperforming ones?

select products.name, products.price
from products
where products.id not in (select orders.item_id from orders);

SELECT products.name, products.price
FROM products
LEFT JOIN orders ON products.id = orders.item_id
WHERE orders.item_id IS NULL;



-- What are all the orders the customers bought?


-- What days had the highest sales? And the lowest?

select orders.date, count(*) as total_orders
from orders
group by orders.date
order by total_orders desc;


SELECT 
  orders.date, 
  products.name AS product_name,
  COUNT(*) AS total_orders
FROM orders
JOIN products ON orders.item_id = products.id
GROUP BY orders.date, products.name
ORDER BY orders.date, total_orders DESC;
