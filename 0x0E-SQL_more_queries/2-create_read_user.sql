-- Creates the database hbtn_0d_2 and user_0d_2
-- user_0d_2 only has the SELECT privilege
CREATE DATABASE
	IF NOT EXISTS `hbtn_0d_2`;
CREATE USER
	IF NOT EXISTS 'user_0d_2'@'localhost'
	IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
	ON `hbtn_0d_2`.*
	TO
	'user_od_2'@'localhost';
