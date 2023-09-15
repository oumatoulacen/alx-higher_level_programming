--  creates the database hbtn_0d_usa and the table states

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXIST states (
	id INT NOT NULL PRIMARY KEY AUTO_INCTEMENT;
	name VARCHAR(256) NOT NULL
	);
