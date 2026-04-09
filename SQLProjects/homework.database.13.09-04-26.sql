use northwind;

-- task1 Выберите только те строки из таблицы suppliers, где company имеет значение Supplier A
select *
from northwind.suppliers;

select *
from northwind.suppliers
where company like '%A';

-- task2 Вывести все строки там, где purchase_order_id не указано. При этом дополнительно создать столбец total_price как произведение quantity * unit_price
select id, purchase_order_id, quantity, unit_price, sum(quantity * unit_price) as total_price
from northwind.order_details
where purchase_order_id is null
group by id;

-- task3 Выведите какая дата будет через 51 день
select DATE_ADD(CURDATE(), interval 51 day);

-- task4 Посчитайте количество уникальных заказов purchase_order_id
select count(distinct purchase_order_id) as unicue_purchase_order_id
from northwind.order_details;

-- task5 Выведите все столбцы таблицы order_details, а также дополнительный столбец payment_method из таблицы purchase_orders. Оставьте только заказы для которых известен payment_method
select od.*, po.payment_method
from northwind.order_details od
left join northwind.purchase_orders po on od.purchase_order_id = po.id
where po.payment_method is not null;