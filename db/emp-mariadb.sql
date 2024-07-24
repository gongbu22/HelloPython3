drop table emp;

delete from emp;

create table emp (
                     empid   int primary key,
                     fname   varchar(30)     not null,
                     lname   varchar(30)     not null,
                     email   varchar(100)    not null,
                     phone   varchar(15)     not null,
                     hdate   date            not null,
                     jobid   varchar(20)     not null,
                     sal     int         default 0,
                     comm    decimal(5,2)    default 0.00,
                     mgrid   int,
                     deptid  int
);

insert into emp (empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, deptid)
values (100, 'Steven', 'King', 'SKING', '515.123.4567', '2003-06-17', 'AD_PRES', 24000, NULL, NULL, 90);

select * from emp;
