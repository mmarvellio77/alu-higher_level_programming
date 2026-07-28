# SQL More Queries

Advanced SQL project covering MySQL user privileges, joins, and more complex queries.

## Requirements

- All SQL queries validated on MySQL 8.4 (Aiven-hosted server)
- Comments are required at the beginning of each file
- All files should end with a new line
- All SQL keywords should be in uppercase

## Tasks

### 0. My privileges!

`0-privileges.sql` - Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the server, using `information_schema.USER_PRIVILEGES` and `information_schema.SCHEMA_PRIVILEGES` so the script doesn't error out even if a user has no grants defined.
