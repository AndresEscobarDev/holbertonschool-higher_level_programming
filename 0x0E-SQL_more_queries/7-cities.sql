-- Script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- Create new hbtn_0d_usa database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use hbtn_0d_usa database.
USE hbtn_0d_usa;
-- Create new cities table in hbtn_0d_usa.
CREATE TABLE IF NOT EXISTS cities (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id));
