--1. Add index to improve search on orders.customer_id
CREATE INDEX idx_orders_customer_id 
ON orders(customer_id);

--2. Use EXPLAIN to analyze query
EXPLAIN 
SELECT * FROM orders 
WHERE customer_id = 101;

--3. Optimize a slow join query

SELECT 
    c.name, 
    o.order_date, 
    o.amount 
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id;

--4. Explain when an index should NOT be used
/*
1. Tiny Tables
If a table only has a few rows, it is actually faster for the database to just read the whole
 table than to waste time looking up an index first.

2. Write-Heavy Tables
Every time you INSERT, UPDATE, or DELETE data, the database also has to update the index.If 
a table gets updated constantly (like a live log file), an index will severely slow down the 
system.

3. Columns with "Low Cardinality"
Don't index columns that only have a few possible values (like Status: Active/Inactive,
True/False, or Gender: M/F). The index doesn't narrow the search down enough to be useful.

4. Frequently Changing Columns
If the data in a specific column changes all the time, constantly rebuilding an index on that
 column will drain your database's performance.

5. Rarely Searched Columns
If a column is almost never used in a WHERE filter or a JOIN condition, indexing it is just a
 waste of computer storage space!

*/