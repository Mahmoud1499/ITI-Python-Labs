CREATE DATABASE IF NOT EXISTS pythonlab;
USE pythonlab;

CREATE TABLE IF NOT EXISTS employee (
  id INTEGER PRIMARY KEY auto_increment,
  first_name TEXT,
  last_name TEXT,
  age INTEGER,
  department TEXT,
  salary INTEGER
  managed_department TEXT

);