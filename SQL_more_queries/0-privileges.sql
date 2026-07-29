-- List users to verify they exist
SELECT user, host FROM mysql.user WHERE user IN ('user_0d_1', 'user_0d_2');

-- Show privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
