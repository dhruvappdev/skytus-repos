--1. Display employee name with department name
SELECT 
    e.emp_name, 
    d.dept_name 
FROM 
    employees e
JOIN 
    departments d ON e.dept_id = d.dept_id;

--2. Display employees earning more than 50,000
SELECT 
    * FROM 
    employees 
WHERE 
    salary > 50000;

--3. Display department-wise total salary
SELECT 
    d.dept_name, 
    SUM(e.salary) AS total_salary 
FROM 
    employees e
JOIN 
    departments d ON e.dept_id = d.dept_id
GROUP BY 
    d.dept_name;

--4. Display departments with more than 2 employees
SELECT 
    d.dept_name, 
    COUNT(e.emp_id) AS employee_count 
FROM 
    employees e
JOIN 
    departments d ON e.dept_id = d.dept_id
GROUP BY 
    d.dept_name
HAVING 
    COUNT(e.emp_id) > 2;

--5. Display employees without a department
SELECT 
    * FROM 
    employees 
WHERE 
    dept_id IS NULL;

