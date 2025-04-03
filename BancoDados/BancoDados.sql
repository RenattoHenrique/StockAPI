-- Criação do banco de dados  
CREATE DATABASE `stock`;  

-- Selecionando o banco de dados  
USE `stock`; 

-- Criação da tabela products  
CREATE TABLE `products` (  
    `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,  
    `name` VARCHAR(50) NOT NULL,  
    `supplier` VARCHAR(50) NOT NULL,  
    `cost` DECIMAL(10, 2) NOT NULL,  
    `price` DECIMAL(10, 2) NOT NULL,  
    PRIMARY KEY (`id`)  
);  

SELECT * FROM products;