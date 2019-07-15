-- converts hbtn_0c_0 database and selected elements to UTF8

-- convert the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- convert the table
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4
 COLLATE utf8mb4_unicode_ci;
