use 121225ptm_Red_Hats_Sysytem_JCC_Weapon;
drop table employees_12;
create table employees_12
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name varchar(20), 
    last_name varchar(20),
    age int,
    salary decimal(10, 2),
    department varchar(50)
);

insert into employees_12 (first_name, last_name, age, salary, department)
value
('Иван', 'Петров', 28, 75000, 'IT'),
('Анна', 'Смирнова', 34, 92000, 'HR'),
('Дмитрий', 'Кузнецов', 45, 115000, 'Sales'),
('Елена', 'Соколова', 23, 58000, 'Marketing'),
('Михаил', 'Попов', 31, 89000, 'IT');

-- task1 Вывести id департамента, в котором работает сотрудник, в зависимости от Id сотрудника.
select *
from employees_12;

drop PROCEDURE employee_department;
DELIMITER //
CREATE PROCEDURE employee_department(in employee_id int)
BEGIN
 select department from employees_12 where id = employee_id;
END //
DELIMITER ;

call employee_department(2);

-- task2 Создайте хранимую процедуру get_employee_age, которая принимает id сотрудника (IN-параметр) и возвращает его возраст через OUT-параметр.
drop procedure get_employee_age;
DELIMITER //
create procedure get_employee_age(in employee_id int, out employee_age int)
begin
	select age into employee_age from employees_12 where id = employee_id;
end //
DELIMITER ;
set @employee_age = 0;
call get_employee_age(1, @employee_age);
select @employee_age;

-- task3 Создайте хранимую процедуру decrease_salary, которая принимает зарплату сотрудника (INOUT-параметр) и уменьшает ее на 10%.
select *
from employees_12;

drop procedure decrease_salary;
DELIMITER //
create procedure decrease_salary(inout employee_salary int)
begin
	set employee_salary = employee_salary * 0.9;
end //
DELIMITER ;
set @salary = 75000;
call decrease_salary(@salary);
select @salary;
