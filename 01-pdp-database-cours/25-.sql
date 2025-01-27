SELECT productName, SUM(quantityInStock) AS total_quantity
FROM orders
GROUP BY productName
ORDER BY total_quantity DESC
LIMIT 10;  -- Выведем топ-10 продуктов по количеству

SELECT MONTH(orderDate) AS month, YEAR(orderDate) AS year, SUM(quantityInStock) AS total_quantity
FROM orders
GROUP BY month, year
ORDER BY year, month;

SELECT DISTINCT country
FROM orders;

SELECT channel, COUNT(*) AS number_of_orders
FROM orders
GROUP BY channel;


SELECT productName, SUM(quantityOrdered) AS total_quantity_ordered
FROM orders
GROUP BY productName
ORDER BY total_quantity_ordered DESC;


SELECT MONTH(orderDate) AS month, YEAR(orderDate) AS year, SUM(quantityOrdered) AS total_quantity_ordered
FROM orders
GROUP BY month, year
ORDER BY year, month;

SELECT DISTINCT country
FROM orders;

SELECT salesChannel, COUNT(*) AS number_of_orders
FROM orders
GROUP BY salesChannel;

SELECT customerName, SUM(quantityOrdered) AS total_quantity_ordered
FROM orders
GROUP BY customerName
ORDER BY total_quantity_ordered DESC;

SELECT productName, SUM(quantityOrdered) AS total_quantity
FROM orders
GROUP BY productName
ORDER BY total_quantity DESC;


SELECT MONTH(orderDate) AS month, YEAR(orderDate) AS year, SUM(quantityOrdered) AS total_quantity
FROM orders
GROUP BY month, year
ORDER BY year, month;

SELECT customerName, SUM(paymentAmount) AS total_spent
FROM orders
GROUP BY customerName
ORDER BY total_spent DESC
LIMIT 10;

SELECT 
    orderDate,
    SUM(quantityOrdered) AS total_ordered_quantity
FROM orders
GROUP BY orderDate
ORDER BY total_ordered_quantity DESC
LIMIT 10;

select orderDate AS month from orders;


SELECT 
    DATE_FORMAT(orderDate, '%Y-%m') AS order_month, -- Sani YYYY-MM formatida o'zgartiramiz
    SUM(quantityOrdered) AS total_ordered_quantity
FROM orders
GROUP BY order_month
ORDER BY total_ordered_quantity DESC
LIMIT 50000;

SELECT 
    DATE_FORMAT(STR_TO_DATE(orderDate, '%m/%d/%Y'), '%m') AS order_month, -- Sani YYYY-MM formatiga o'zgartirish
    SUM(quantityOrdered) AS total_ordered_quantity
FROM orders
GROUP BY order_month
ORDER BY total_ordered_quantity DESC;
