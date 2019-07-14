CREATE USER IF NOT EXISTS 'bank'@'%' IDENTIFIED BY 'secret';
CREATE USER IF NOT EXISTS 'ie2'@'%' IDENTIFIED BY 'secret';
CREATE USER IF NOT EXISTS 'se2'@'%' IDENTIFIED BY 'secret';

CREATE DATABASE IF NOT EXISTS bank;
GRANT ALL ON bank.* TO 'bank'@'%';

CREATE DATABASE IF NOT EXISTS injectengine;
GRANT ALL ON injectengine.* TO 'ie2'@'%';

CREATE DATABASE IF NOT EXISTS scoreengine;
GRANT ALL ON scoreengine.* TO 'ie2'@'%';
GRANT ALL ON scoreengine.* TO 'se2'@'%';
