登录数据库
=============

本地终端登录
-------------
```
mysql -u 用户名 -p 密码
```

远程登录mysql
------------
```
mysql -u 用户名 -p 密码 -h 地址
```
例子: mysql x-uroot -proots -h127.0.0.1

断开已连接的mysql服务
---------------------------------
可以使用`exit`或者`quit`或者`\q`来断开已经连接的mysql服务

<!--more-->

---

数据库操作
==========

查看数据库
-----------------
```
show databases;
```

创建数据库
-----------------
```php
create database 数据库名;
或
create database 数据库名 [库选项];
库选项：用来约束数据库
```
> a.字符集设定：charset,常用的有：gbk,utf8
> b.校对集设定：具体校对集(数据比较的规则)

例如：create database mydata charset utf8;


删除数据库
----------------
```
drop database 数据库名;
```

选择数据库
-----------------
```
use 数据库名;
```

其他操作
--------------
查看当前数据库信息：` select database();`
查看数据库的环境变量：`show variables;`
查看建库语句：`show database 数据库名;`


---

表操作
======

查看此数据库中的所有表
---------------------------------
```
show tables;
```

创建表
----------
```
create table 表名(字段名 属性,字段名 属性,......);
```
例如：create table user(id int,username varchar(25));

删除表
---------
```
drop tables 表名;
```

查看表结构
-----------------
```
desc 表名;
```

修改表名字
---------------
```
alter table 表名 rename 新表名;
```

其他操作
-------------
查看建表语句：`show create table 表名;`
查看该表在哪个库下：`select database();`

---

字段操作
======

修改字段名
---------------
```
alter table 表名 change 原字段名 新字段名 类型;
```

删除字段
-------------
```
alter table 表名 drop 字段名;
```

插入字段
-------------
```
alter table 表名 add 字段名 类型 位置;

`first` 第一个位置
`after` 在那个字段之后，默认存在表中的最后
```
例如：alter table user add password varchar(45) after username;

修改表字段值
--------------------
```
alter table 表名 modify 字段名 修改后的值;
```

---

索引
====

主键索引(primary key)
------------
唯一 且 不能为空
```
alter table  表名 add primary key (字段名)
```

唯一索引(UNIQUE)
-------------
唯一索引,不允许有重复
```
alter table 表名 add unique(字段名)
```

普通索引(INDEX)
-------------
索引，普通的
```
alter table 表名 add index index_name(字段名)
```

全文索引(FULLTEXT)
------------
全文索引，用于在一篇文章中，检索文本信息的
```
alter talbe 表名 add fulltext(字段名)
```

多列索引
------------
```
alter table 表名 add index index_name(字段名1,字段名2,字段名3,.....)
```

其他操作
-------------
查看添加索引的字段：`show index from 表名`

---

内容操作
=========

插入内容
------------
第一种插入
```
insert into 表名 valuses(内容);
```

根据你添加的字段依次填写

例如：
> desc bbs;
> id,username,password
> insert into bbs values(1,'只因不住地',123456);

第二种插入
```
insert into 表名(字段名) values(内容);

对应上前面的字段名
```

插入多条数据
```
insert into 表名(字段名) values (内容1)(内容2)......;
```

例如
> insert into 表名(id,username,password) values();

查看内容
------------
```
select * from 表名;
```

删除内容
-------------

```
delect from 表名 where 字段名=内容;
```

修改内容
------------
```
update 表名 set 字段=内容 where 条件;
```

例如：update 表名 set username='test' where id=1;

---

查询操作
==========

查看单个字段的所有内容
```
select 字段名 form 表名;
```

去除重复值查看某个内容全部内容
---------------------------------------------
```
select distinct 字段名 from 表名;
```

根据条件查看内容
-------------------------
```
select * from 表名 where 条件;
```

查看id为2的字段全部内容
> select * from bbs where id=2;

区间查看内容
-------------------
```
select * from 表名 where 字段 between 条件1 and 条件2;

select * from 表名 where 字段=条件 or 字段=条件;
```

查看年龄30到40之间的人
> select * from bbs where age between 30 and 40;
> select * from bbs where age=30 or age=40;

取不等于条件的内容
-------------------------------
```
select * from 表名 where 字段 !=内容;
```

年龄不等于50的人
> select * from bbs where age !=50;

固定值查询
------------------
```
select * from 表名 where 字段 in(内容1,内容2,....);
```

模糊查询
-------------
```
select * from 表名 where 字段 like '%内容%';
```

升序查询
-------------
```
select * from 表名 order by 字段;
```

降序查询
------------
```
select * from 表名 order by 字段 desc;
```

limit 查询
------------
```
select * from 表名 limit 0,1;

limit 0,1;
0 表示从第0行开始查询
1 表示显示1条
```

分组
-------
```
select * from 表名 group by 字段名;

根据什么字段分组
```

其别名 as
------------
```
select 字段 as 别名 from 表名;
```

嵌套查询
------------
不推荐使用,效率慢
```
select 字段 from 表名 where 字段 in(select 字段 from 表名);
```

内联查询
------------
```
select 表1.字段 [as 别名],表n.字段 from 表1 inner join 表2 on 条件; 
```

左联查询
-------------
以左表为基准
```
select 表1.字段 [as 别名],表n.字段 from 表1 left join 表n on 条件;
```

右联查询
--------------
以右表为基准
```
select 表1.字段 [as 表名],表n.字段 form 表1 right join 表n on 条件;
```

其他操作
-------------
查询该表有几条数据：`select count(*) from 表名;`

---