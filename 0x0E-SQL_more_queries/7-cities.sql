-- Creates a database htbn_0d_usa and table cities
CREATE DATABASE IF NOT EXISTS `htbn_0d_usa`
CREATE TABLE IF NOT EXISTS `htbn_0d_usa`.`cities` (
	PRIMARY KEY(`id`)
	`id`	INT	NOT NULL  AUTO_INCREMENT,
	`state_id` INT	NOT NULL,
	`name`	VARCHAR(256) NOT NULL,
	FOREIGN KEY(`state_id`)
	REFERENCES `hbtn_0d_usa`(`id`)
);	
