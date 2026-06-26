--1. Find the Nth highest salary
SELECT DISTINCT 
    salary 
FROM 
    employees 
ORDER BY 
    salary DESC 
LIMIT 1 OFFSET 2;

--2. Remove duplicate records
WITH DuplicateCTE AS (
    SELECT 
        *, 
        ROW_NUMBER() OVER(
            PARTITION BY first_name, last_name, email -- Columns that make it a duplicate
            ORDER BY emp_id -- Keeps the lowest ID
        ) as row_num
    FROM 
        employees
)
DELETE FROM DuplicateCTE WHERE row_num > 1;

--3. Find records common in two tables
SELECT 
    t1.emp_id, 
    t1.emp_name 
FROM 
    table1 t1
INNER JOIN 
    table2 t2 ON t1.emp_id = t2.emp_id;

--4. Find employees hired in last 6 months
SELECT 
    * FROM 
    employees 
WHERE 
    hire_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH);

--5. Find continuous duplicate values
SELECT 
    * FROM (
    SELECT 
        emp_id, 
        department, 
        LAG(department) OVER (ORDER BY emp_id) AS previous_department
    FROM 
        employees
) AS subquery
WHERE 
    department = previous_department;