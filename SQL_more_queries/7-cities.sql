--  a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT states FOREIGN KEY (state_id) REFERENCES states(id)
);
