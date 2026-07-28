cat << 'EOF' > 0-privileges.sql
-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
EOF
