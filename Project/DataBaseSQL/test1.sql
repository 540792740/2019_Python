create database db_test;
drop database test1;
use db_test;
create  table t_student(
id int(4) primary key,
s_name VARCHAR(200) not null,
address varchar(200)
);

select * from emp;

select empno, job, ename from emp;

select ename, sal * 12 as Salary from emp;


-- 去重，选择出来
select distinct deptno from emp;


-- 排序, 默认升序， 最后加一个desc就是降序
select ename, sal, from emp order by sal;
select ename, sal, from emp order by sal, ename;


--  条件查询，1000 < sal < 2000
select ename, sal from emp where sal > 1000 and sal < 2000 order by sal desc;


-- 优先级：
-- 算数计算 > 连接符 > 比较 > 逻辑


-- 分页查询
-- 每页显示五条：（从第几个开始取， 取几行）
select * from emp limit 0, 5;
select * from emp limit 5, 5;