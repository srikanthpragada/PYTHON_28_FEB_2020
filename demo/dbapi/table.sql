CREATE TABLE employees (
    id       INTEGER      PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR (30) NOT NULL,
    salary   INTEGER (6)  NOT NULL,
    job      VARCHAR (5)
);


insert into employees (fullname,salary,job) values('Larry Page',120000,'CTO')
insert into employees (fullname,salary,job) values('Tim Cook',220000,'CEO')
insert into employees (fullname,salary,job) values('Anders',140000,'SRPROG')
