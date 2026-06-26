--1. Start a transaction
START TRANSACTION;

--2. Insert record into accounts
INSERT INTO accounts (account_id, user_name, balance) 
VALUES (101, 'Rahul', 5000.00);

--3. Rollback changes
ROLLBACK;

--4. Commit valid transactions
COMMIT;

--5. Demonstrate transfer of money using transaction
-- Step 1: Start the safe zone
START TRANSACTION;

-- Step 2: Deduct $500 from Account A
UPDATE accounts 
SET balance = balance - 500 
WHERE account_id = 1;

-- Step 3: Add $500 to Account B
UPDATE accounts 
SET balance = balance + 500 
WHERE account_id = 2;

-- Step 4: If both updates succeeded, lock it in!
COMMIT;