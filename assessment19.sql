--1. Create users Table with Constraints
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255) NOT NULL
);

--2. Add Foreign Key Between orders and users
ALTER TABLE orders
ADD CONSTRAINT fk_user_id
FOREIGN KEY (user_id) REFERENCES users(user_id);

--3. Create Index on Email Column
CREATE INDEX idx_email 
ON users(email);

--4. Create View for User Order Summary
CREATE VIEW user_order_summary AS
SELECT 
    u.user_id, 
    u.email, 
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS lifetime_spent
FROM 
    users u
LEFT JOIN 
    orders o ON u.user_id = o.user_id
GROUP BY 
    u.user_id, u.email;