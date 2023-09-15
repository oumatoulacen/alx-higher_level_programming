--  creates the database hbtn_0d_usa and the table states

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXIST states (
	id INT UNIQUE primaty key auto_increment;
	name VARCHAR(256) not NULL
	);
