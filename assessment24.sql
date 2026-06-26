--Part 1: Tables & Relationships
-- 👤 1. Members Table (Primary Data)
CREATE TABLE Members (
    member_id INT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    room_number VARCHAR(10),
    phone_number VARCHAR(15),
    join_date DATE
);

-- 📜 2. Menu Table (Food & Costs)
CREATE TABLE Menu (
    meal_id INT PRIMARY KEY,
    meal_name VARCHAR(100),
    meal_type VARCHAR(50), -- e.g., Breakfast, Lunch, Dinner
    price DECIMAL(6, 2)
);

-- 📅 3. Meal Logs (Relationship: Connects Members to Meals)
CREATE TABLE Meal_Logs (
    log_id INT PRIMARY KEY,
    member_id INT,
    meal_date DATE,
    meal_type VARCHAR(50),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

-- 💰 4. Payments (Relationship: Connects Members to Finances)
CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    member_id INT,
    amount DECIMAL(8, 2),
    payment_date DATE,
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

--Part 2: Sample Data Insertion
-- 📥 Inserting Members
INSERT INTO Members (member_id, full_name, room_number, phone_number, join_date) VALUES
(1, 'Rahul Sharma', '101A', '9876543210', '2026-06-01'),
(2, 'Priya Patel', '205B', '9876543211', '2026-06-05'),
(3, 'Amit Kumar', '101A', '9876543212', '2026-06-10');

-- 📥 Inserting Menu Items
INSERT INTO Menu (meal_id, meal_name, meal_type, price) VALUES
(101, 'Poha & Jalebi', 'Breakfast', 40.00),
(102, 'Dal Roti Sabzi', 'Lunch', 80.00),
(103, 'Paneer Butter Masala', 'Dinner', 120.00);

-- 📥 Inserting Meal Logs (Attendance)
INSERT INTO Meal_Logs (log_id, member_id, meal_date, meal_type) VALUES
(1001, 1, '2026-06-26', 'Breakfast'),
(1002, 1, '2026-06-26', 'Lunch'),
(1003, 2, '2026-06-26', 'Lunch');

-- 📥 Inserting Payments
INSERT INTO Payments (payment_id, member_id, amount, payment_date) VALUES
(5001, 1, 1500.00, '2026-06-02'),
(5002, 2, 2000.00, '2026-06-06');

--Part 3: 15 Essential Business Queries
--Member Management

--1. View all currently registered members:
SELECT * FROM Members ORDER BY join_date DESC;

--2. Find members living in a specific room (e.g., '101A'):
SELECT full_name, phone_number FROM Members WHERE room_number = '101A';

--3. Count the total number of active members:
SELECT COUNT(*) AS total_members FROM Members;

--4. Find members who joined in the current month:
SELECT * FROM Members WHERE EXTRACT(MONTH FROM join_date) = 6;

--Menu & Food Management

--5. View the complete menu with prices:
SELECT meal_name, meal_type, price FROM Menu ORDER BY price ASC;

--6. Show only Breakfast items:
SELECT meal_name, price FROM Menu WHERE meal_type = 'Breakfast';

--7. Find the most expensive meal on the menu:
SELECT meal_name, price FROM Menu ORDER BY price DESC LIMIT 1;

--Daily Operations & Logs

--8. View all meals consumed today (e.g., '2026-06-26'):
SELECT * FROM Meal_Logs WHERE meal_date = '2026-06-26';

--9. Count how many people ate Lunch today:
SELECT COUNT(*) AS lunch_count FROM Meal_Logs WHERE meal_date = '2026-06-26' AND meal_type = 'Lunch';

--10. Display a specific member's total meal attendance history:
SELECT m.full_name, COUNT(l.log_id) AS total_meals_eaten
FROM Members m
JOIN Meal_Logs l ON m.member_id = l.member_id
GROUP BY m.full_name;

--11. Find members who skipped meals completely today (Subquery):
SELECT full_name FROM Members 
WHERE member_id NOT IN (SELECT member_id FROM Meal_Logs WHERE meal_date = '2026-06-26');

--Financial Tracking

--12. View all payments made by a specific member (e.g., Rahul):
SELECT amount, payment_date FROM Payments WHERE member_id = 1;

--13. Calculate total revenue collected this month:
SELECT SUM(amount) AS total_monthly_revenue FROM Payments;

--14. Find the largest single payment made:
SELECT m.full_name, p.amount 
FROM Payments p
JOIN Members m ON p.member_id = m.member_id
ORDER BY p.amount DESC LIMIT 1;

--15. Display a financial summary (Total Paid) for every member:
SELECT m.full_name, SUM(p.amount) AS total_amount_paid
FROM Members m
LEFT JOIN Payments p ON m.member_id = p.member_id
GROUP BY m.full_name;

--Part 4: Query Optimization

--Optimization 1: Indexing Foreign Keys
CREATE INDEX idx_payments_member_id ON Payments(member_id);

--Optimization 2: Indexing Dates for Daily Operations
CREATE INDEX idx_meal_logs_date ON Meal_Logs(meal_date);

--Optimization 3: Avoiding SELECT *
SELECT * FROM Members ORDER BY join_date DESC;

SELECT member_id, full_name FROM Members ORDER BY join_date DESC;

