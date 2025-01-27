select * from products;

SELECT LEFT(productCode, 3) AS brandCode, SUM(quantityOrdered) AS totalSold
FROM orders
GROUP BY brandCode
ORDER BY totalSold DESC
LIMIT 5;

SELECT LEFT(productCode, 3) AS brandCode, SUM(quantityOrdered) AS totalSold
FROM orders
GROUP BY brandCode
ORDER BY totalSold DESC
LIMIT 5;


SELECT productName, quantityInStock, SUM(quantityOrdered) AS totalOrdered
FROM orders
GROUP BY productName, quantityInStock
HAVING quantityInStock = 0
ORDER BY totalOrdered DESC;