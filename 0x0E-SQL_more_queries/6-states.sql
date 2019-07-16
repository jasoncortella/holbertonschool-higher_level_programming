-- creates the database hbtn_0d_usa and the table states on your MySQL server.
   -- states description:
      -- id INT unique - auto generated, cant be null, is a primary key
      -- name VARCHAR(256) - can't be null
   -- The database name will be passed as an argument of the mysql command
   -- If the table hbtn_0d_usa already exists, script should not fail
   -- If the table states already exists, script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
       (id INT UNIQUE NOT NULL AUTO_INCREMENT,
       name VARCHAR(256));
