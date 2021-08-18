create database db;
use db;
create table Books(bid varchar(30) primary key, title varchar(20), author varchar(20), availability varchar(20));
create table Books_issued(bid varchar(30) primary key, issuedto varchar(30));