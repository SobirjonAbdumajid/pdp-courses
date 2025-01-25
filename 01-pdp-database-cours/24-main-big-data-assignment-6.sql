# Mijozlar bo‘yicha eng ko‘p buyurtma bergan mamlakatlar qaysilar? 
SELECT country, COUNT(DISTINCT customerName) AS totalCustomers
FROM orders
GROUP BY country
ORDER BY totalCustomers DESC;


# Top 10 eng ko‘p mahsulot buyurtma qilgan mijozlar
SELECT customerName, SUM(quantityOrdered) AS totalProductsOrdered
FROM orders
GROUP BY customerName
ORDER BY totalProductsOrdered DESC
LIMIT 10;


# Eng ko‘p buyurtma qilingan mahsulotlar qaysilar?
SELECT productName, SUM(quantityOrdered) AS totalOrdered
FROM orders
GROUP BY productName
ORDER BY totalOrdered DESC
LIMIT 5;


# Hozirda zaxirada qolgan, ammo talab yuqori bo‘lgan mahsulotlar qaysilar?
SELECT productName, quantityInStock, SUM(quantityOrdered) AS totalOrdered
FROM orders
GROUP BY productName, quantityInStock
HAVING quantityInStock > 0 AND totalOrdered > 100
ORDER BY totalOrdered DESC;


# Eng ko‘p mahsulot sotuvchilari qaysi brendlar?
SELECT LEFT(productCode, 3) AS brandCode, SUM(quantityOrdered) AS totalSold
FROM orders
GROUP BY brandCode
ORDER BY totalSold DESC
LIMIT 5;


# Buyurtma berilgan, ammo zaxirada qolmagan mahsulotlar qaysilar?
SELECT productName, quantityInStock, SUM(quantityOrdered) AS totalOrdered
FROM orders
GROUP BY productName, quantityInStock
HAVING quantityInStock = 0
ORDER BY totalOrdered DESC;

