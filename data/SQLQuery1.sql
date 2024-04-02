DROP DATABASE testmockdata;
CREATE DATABASE testmockdata CHARACTER SET utf8 COLLATE utf8_general_ci;
USE testmockdata; 
CREATE TABLE Category (
	IdCate INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NameCate VARCHAR(20) NOT NULL
);
ALTER TABLE Category 
	AUTO_INCREMENT = 1;
INSERT INTO Category (NameCate) VALUES 
	('Category 1'), 
    ('Category 2'), 
    ('Category 3'), 
    ('Category 4'), 
    ('Category 5');
CREATE TABLE Products (
	IdPro INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NamePro VARCHAR(30) NOT NULL,
    Qty INT NOT NULL, 
    Price FLOAT NOT NULL, 
    ProDesc VARCHAR(50), 
    IdCate INT NOT NULL, 
    FOREIGN KEY(IdCate) REFERENCES Category(IdCate)
);
-- Execute when you need to view data :) 
SELECT *
FROM Category;
SELECT *
FROM Products;
DELETE FROM Products;
