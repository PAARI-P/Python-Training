use college;

create table dept(
dept_id int primary key,
dept_name varchar(30)
);

drop table student;

insert into dept values(1101,'cse');
insert into dept values(1102,'eee');
insert into dept values(1103,'civil');
insert into dept values(1104,'ece');

create table student(
std_id int primary key,
std_name varchar(20),
dept_id int,
FOREIGN KEY (dept_id) REFERENCES dept(dept_id)
);


drop table dept;
insert into student value(1,'abi',1101);
insert into student value(2,'ajai',1102);
insert into student value(3,'elam',1103);
insert into student value(4,'bala',1104);

select * from student;