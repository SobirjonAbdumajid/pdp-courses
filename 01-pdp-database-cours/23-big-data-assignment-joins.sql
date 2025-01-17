SELECT 
    c.customerName,
    c.contactFirstName,
    c.contactLastName,
    c.country,
    o.orderNumber,
    o.orderDate,
    o.status,
    o.comments,
    od.productCode,
    p.productName,
    p.quantityInStock,
    od.quantityOrdered,
    od.priceEach,
    pay.amount AS paymentAmount
FROM 
    customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN products p ON od.productCode = p.productCode
LEFT JOIN payments pay ON c.customerNumber = pay.customerNumber;


select * from customers;
select * from orders;
select * from orderdetails;
select * from products;
select * from payments;