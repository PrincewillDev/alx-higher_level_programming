-- This script converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- It converts the database, table and field
USE hbtn_0c_0
ALTER DATABASE hbtn_0c_0 CHARACTER
SET
    utf8mb4 COLLATE utf8mb4_unicode_ci
ALTER TABLE first_table CONVERT TO CHARACTER
SET
    utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER first_table CHANGE name name VARCHAR(255) CHARACTER
SET
    utf8mb4 COLLATE utf8mb4_unicode_ci;