USE defaultdb;
CREATE DATABASE IF NOT EXISTS dineright; 

USE dineright;

CREATE TABLE IF NOT EXISTS accounts (
  email STRING PRIMARY KEY,
  name STRING,
  password STRING,
  profile_pic STRING
);
