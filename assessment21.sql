--1. Total orders per customer
SELECT 
    c.name, 
    COUNT(o.order_id) AS total_orders
FROM 
    customers c
LEFT JOIN 
    orders o ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_id, c.name;

--2. Customers who never placed an order
SELECT 
    * FROM 
    customers 
WHERE 
    customer_id NOT IN (SELECT customer_id FROM orders);

--3. Highest selling product
SELECT 
    p.product_name, 
    SUM(oi.quantity) AS total_quantity_sold
FROM 
    products p
JOIN 
    order_items oi ON p.product_id = oi.product_id
GROUP BY 
    p.product_id, p.product_name
ORDER BY 
    total_quantity_sold DESC
LIMIT 1;

--4. Monthly sales report
SELECT 
    EXTRACT(YEAR FROM order_date) AS sales_year,
    EXTRACT(MONTH FROM order_date) AS sales_month,
    SUM(amount) AS monthly_revenue
FROM 
    orders
GROUP BY 
    sales_year, sales_month
ORDER BY 
    sales_year DESC, sales_month DESC;

--5. Customers with total purchase > ₹50,000
SELECT 
    c.name, 
    SUM(o.amount) AS total_spent
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_id, c.name
HAVING 
    SUM(o.amount) > 50000;

--6. Top 3 cities by revenue
SELECT 
    c.city, 
    SUM(o.amount) AS total_revenue
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
GROUP BY 
    c.city
ORDER BY 
    total_revenue DESC
LIMIT 3;