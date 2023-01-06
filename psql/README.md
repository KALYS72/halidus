# Slash commands\

* \c - показывает к какой бд мы подключены и через какого юзера
* \c name_of_db - подключаемся к этой бд
* \l - список вссех бд
* \du - показывает список юзером с их правами
* \dt - показывает список таблиц в текущей бд
* \d+ - показывает более подробную информацию о таблицах
* \q - выход из субд (psql)

# Cоздание баз данных и таблиц
```sql
CREATE DATABASE name_of_db;
--создает базу данных
```

```sql
CREATE TABLE name_of_table (
    column1 data_type1,
    column2 data_type2,
    ...
)
--создает таблицу с полями
```

```sql
DROP DATABASE name_of_db
--удаление базы данных
```


```sql
DROP TABLE name_of_table
--удаление таблицы
```


# Заполнение таблиц
```sql
INSERT INTO name_of_table VALUES
(cal1, val2),
(val2.1, val2.2);
--запись данных в таблицу (заполнение всех полей)
```
```sql
INSERT INTO name_of_table (column1, column2) VALUES
(val1.1, val1.2),
(val2.1, val2.2);
--запись  определенных полей в таблицу
```


# Измененние таблиц
```sql
ALTER TABLE name_of_table ADD COLUMN col_name type
constraint;
--добовляет новую колонку в таблицу 
```
```sql
AlTER TABLE name_of_table DROP column col_name;
-- удаляет колонку из таблицы
```
```sql
alter table name_of_table add constraint constr_name 
constraint;
--добовление ограничения на поле
alter table test add constraint col_unq UNIQUE (col);
-- test- назв таблицы
-- col- назв поля
alter table test add constraint fk_test_test2 foreign key (test2_id) references test2 (id);

sql
alter table name_of_table rename column old_name to new name_name;
--переименовать поле
sql
alter table name_of_table alter column col_name SET data type new_data_type;
alter table name_of_table alter column col_name type new_data_type;
-- изменение типа данных у поля
```


# Вывод данных из таблицы 
```sql
SELECT * FROM name_of_table;
--получение всех записей с таблицы (всех полей)
```
```sql
select name, 
case when (monthlymaintenance > 100)
then 'expensive'
else 'cheap'
end
as cost
from cd.facilities;
--if, elif прямо в  psql
```


# Удаление записей из таблицы
```sql
DELETE FROM name_of_table;
--удаление всех записей из таблицы
```


# Условия 
```sql
DELETE FROM name_of_table WHERE column1 = value1;
--удаление всех соответсвующих этому условию
```



# Обновление записей в таблице

```sql
UPDATE name_of_table SET_col = new_val;
--обновление всех записей в таблице
UPDATE name_of_table SET_col = new_val WHERE ;
```

# import / export без данных

write from file to db

```bash
psql db_name = file.sql
# db_name должна существовать в postgresql
```

write from db to file
```bash
pg_dump_db_name = 
```


```sql
SELECT * FROM name_of_table WHERE title like '%world%';
--выбирает все записи у которых в поле есть название содержащие 'world'
--hello world
--world
--world hello

--like - чувствителен к регистру (World - не пройдет)
```

```sql
SELECT * FROM name_of_table WHERE title ilike
'%word%'
--ilike - не чувствителен к регистру
--WORLD
--world
--worlD
--world HELLO
--HEllo WORLD hello
```

```sql
SELECT * FROM name_of_table ORDER BY column1;
--сортировка по возрастанию column1 (если str то по алфавитному порядку в 1 букве)
```

```sql
SELECT * FROM name_of_table ORDER BY column1 DESC;
--сортировка по убыванию column1 (если str то по алфавитному порядку в 1 букве)
```

```sql
SELECT * FROM name_of_table LIMIT 10
--выводит первые 10 записей
```

```sql
SELECT * FROM name_of_table OFFSET 10
--пропускает первые 10 записей
```

```sql
SELECT * FROM name_of_table LIMIT 5 OFFSET 10
--пропускает первые 10 записей
--выбирает следующие 5 записей
```

# Связи

## pk fk
> **primary key (pk)** - первичный ключ, ограничение, которое накладывается на поле, которое будет использовано в связях (создает btree для быстрого поиска)

>**foreign key (fk)** - первичный ключ, ограничение, которое накладывается на поле, которое ссылается на pk в другой таблице

```sql
CREATE TABLE author (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE book (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    published YEAR,
    author_id INT

    CONSTRAINT fk_book_author FOREIGN KEY (author_id)
    REFERENCES author (id)
)
```


## Виды связи
> One to one - один к одному
* один пользователь - один ID
* один автор - одна автобиография

> One to many - один ко многим
* один блогер - много постов
* один куратор - много студентов
* один продукт - много комментариев

> Many to many - многие ко многим
* один ментор - много студентов, один студент - много менторов 
* один разработчик - много проектов, один проект - много разработчиков
* один банк - много клиентов, один клиент - много банков

## Виды связей (практика)
### One to one
```sql
CREATE TABLE author (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

CREATE TABLE autobiography (
    if SERIAL PRIMARY KEY,
    body TEXT,
    created_at DATE,
    author_id INT UNIQUE, --unique мы ставим, чтобы сделать one 2 one;
    CONSTRAINT fk_author_bio FOREIGN KEY (author_id) REFERENCES author(id)
);
```
### One to many
```sql
CREATE TABLE curator (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    language VARCHAR(2),
    curator_id INT,

    CONSTRAINT fk_student_curator
    FOREIGN KEY (curator_id) REFERENCES curator (id)
);
```

### Many to many
```sql
CREATE TABLE developer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    experience INT
);

CREATE TABLE project (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    tz TEXT,
    start DATE,
    finish DATE
);

CREATE TABLE dev_proj (
    dev_id INT,
    proj_id INT,

    CONSTRAINT fk_dev FOREIGN KEY (dev_id) REFERENCES developer (id),
    CONSTRAINT fk_proj FOREIGN KEY (proj_id) REFERENCES project (id)
);
```

## Joins
> **JOIN** - инструкция, которая позволяет в запросах SELECT брать данные из нескольких таблиц

> INNER **JOIN** (**JOIN**) - достаются только те записи, у которых есть связь

> FULL **JOIN** - достаются записи с обеих таблиц

> LEFT **JOIN** - достает все записи с левой таблицы, и с правой таблицы у которых есть связь с левой таблицы

> RIGHT **JOIN** - достает все записи с правой таблицы, и с левой таблицы у которых есть связь с правой таблицы

> где 'правая' таблица - та которая написана до join
> а 'левая' таблица - та, которая написана после join



# Практика

## blog
```sql
--создание таблицы
CREATE TABLE author (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE book (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    published YEAR,
    author_id INT

    CONSTRAINT fk_book_author FOREIGN KEY (author_id)
    REFERENCES author (id)
)

--заполнение таблицы
INSERT INTO blogger (name) VALUES ('blogger 1'), ('blogger 2'), ('blogger 3'); 

INSERT INTO post (blogger_id, body, created_at) VALUES
(1, 'my first blog', '01.08.2020'),
(1, 'today is a good day', '09.02.2020'),
(1, 'it is my b-day!', '09.30.2021');

INSERT INTO post (blogger_id, body, created_at) VALUES
(2, 'my first post', '05.10.2013'),
(2, 'some post', '06.06.2022');

INSERT INTO post (blogger_id, body, created_at) VALUES
(3, 'i am not a blogger', '12.08.2022');


```

## shop 
```sql
--создание таблицы
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    price DECIMAL
);

CREATE TABLE cart (
    id SERIAL PRIMARY KEY,
    customer_id INT,
    product_id INT,

    CONSTRAINT cart_customer FOREIGN KEY (customer_id) REFERENCES customer (id), 
    CONSTRAINT cart_product FOREIGN KEY (product_id) REFERENCES product (id)
);

--заполнение таблицы
INSERT INTO customer (name) VALUES ('customer 1'), ('customer 2'), ('customer 3'); 

INSERT INTO product (title, price) VALUES
('product 1', 340),
('product 2', 503),
('product 3', 470),
('product 4', 236),
('product 5', 452);

INSERT INTO cart (customer_id, product_id) VALUES
(1, 1), (1, 2), (1, 4),
(2, 3),
(3, 4), (3, 5);
```


# Агрегатные функции
> SUM - функция, считающая сумму всех записей в сгруппированном поле
```sql
--пример из shop
SELECT customer.name, SUM(product.price) AS total_price
FROM product JOIN cart on product.id = cart.product_id
JOIN customer ON customer.id = cart.customer_id
GROUP BY (customer.name);
--     name    | total_price 
-- ------------+-------------
--  customer 2 |         470
--  customer 3 |         688
--  customer 1 |        1079
```

> ARRAY_AGG - обьединяет записи сгруппированного поля в массив
```sql
--пример из blog
SELECT blogger.name, ARRAY_AGG(post.body)
FROM blogger JOIN post ON blogger.id = post.blogger_id
GROUP BY (blogger.name);
--    name    |                         array_agg                         
-- -----------+-----------------------------------------------------------
--  blogger 2 | {"my first post","some post"}
--  blogger 1 | {"my first blog","today is a good day","it is my b-day!"}
--  blogger 3 | {"i am not a blogger"}
```

> MIN, MAX - высчитывает миинимальное и максимальное значение среди записей в сгруппированном виде
```sql
--пример из post
SELECT blogger.name, MIN(post.created_at) AS first, MAX(post.created_at) AS last
FROM blogger JOIN post on blogger.id = post.blogger_id
GROUP BY (blogger.name);
--    name    |   first    |    last    
-- -----------+------------+------------
--  blogger 2 | 2013-05-10 | 2022-06-06
--  blogger 1 | 2020-01-08 | 2021-09-30
--  blogger 3 | 2022-12-08 | 2022-12-08
```

> COUNT - считает кол-во записей в сгруппированном поле
```sql
--пример из post
SELECT blogger.name, COUNT(post.id) AS posts_count
FROM blogger JOIN post on blogger.id = post.blogger_id
GROUP BY (blogger.name); 
--    name    | posts_count 
-- -----------+-------------
--  blogger 2 |           2
--  blogger 1 |           3
--  blogger 3 |           1
```