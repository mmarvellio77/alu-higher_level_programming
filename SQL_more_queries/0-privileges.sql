-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2
SELECT
    grantee,
    privilege_type
FROM
    information_schema.USER_PRIVILEGES
WHERE
    grantee LIKE '%user_0d_1%'
    OR grantee LIKE '%user_0d_2%'

UNION

SELECT
    grantee,
    privilege_type
FROM
    information_schema.SCHEMA_PRIVILEGES
WHERE
    grantee LIKE '%user_0d_1%'
    OR grantee LIKE '%user_0d_2%';
