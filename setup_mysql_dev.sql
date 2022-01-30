-- prepares a MySQL server for the project
-- FLUSH PRIVILEGES; when we grant some privileges for a user,
-- running the command flush privileges will reloads the grant tables
-- in the mysql database enabling the changes to take effect
-- without reloading or restarting mysql service
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
