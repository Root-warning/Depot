---
title: MongoDB基础学习
tags: windows
categories:
  - 随手记
abbrlink: 8c3b0bac
---

# 简介
`分布式数据库`：由多态计算机和通讯的软件组件通过计算机网络组成的，建立在网络之上的软件系统
MongoDB是一个基于分布式文件存储的数据库，由C++编写
在高负载的情况下，添加更多的节点，可以保证服务器性能
MongoDB下的shell的交互式是采用Javascript shell进行操作和管理的
当进入后台时，它会默认链接到数据库

# cmd下运行MongoDB服务器
```
mongod --dbpath data文件
```

---

# 连接MongoDB
```
mongo
```

<!--more-->

标准连接语法
```
mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
```
* `mongodb://`：固定格式
* `username:password@`（可选项）：如果设置，在连接数据库服务器之后，驱动都会尝试登陆这个数据库
* `host`：指定要连接服务器的地址，要多连接，就指定多个主机地址
* `post`：指定改的端口，不填默认为27017
* `/database`：连接并验证登陆指定数据库，若不指定，默认打开test库
* `?options`：连接选项，如果不使用database，则前面需加上 / 

---

# 安装MongoDB服务

* 方案一
```
mongod.exe --config "C:\Program Files\MongoDB\Server\4.0\bin\mongod.cfg" --install
```

* 方案二
```
mongod --logpath c:\mongodb\log\mongodb.log --logappend --dbpath c:\mongodb\db --directoryerdb --serviceName MongoDB --install
```


## 启动和停止
需超级管理权限
```
# 启动
net start MongoDB

# 停止
net stop MongoDB
```

## 移除服务
```
mongod --remove
```

---

# 更改端口
`mongod.cfg`文件中进行修改


进行连接的时候由于更改了端口，所以我们不能直接进行连接
```
mongo 127.0.0.1:new port
```

---

# 用户权限

权限|说明
--|--
Read|运行用户读取指定数据库
readWrite|运行用户读写指定数据库
dbAdmin|允许用户在指定数据库中执行管理函数
userAdmin|允许用户想system.users集合写入，可以找指定数据库里创建，删除和管理用户
clusterAdmin|只在admin数据库中可用，赋予用户所有分片和赋值集相关函数的管理权限
readAnyDatabase|只在admin数据库中可用，赋予用户所有数据库读写权限
userAdminAnyDatabase|只在admin数据库中可用，赋予用户所有数据库的userAdmin权限
dbAdminAnyDatabase| 只在admin数据库中可用，赋予用户所有数据库的dbAdmin权限
root|超级账户管理员，只在admin数据库中可用

## 用户创建语法
```
{
user: "<name>",
pwd: "<password>",
customData: { <any information>},
roles: [
{ role: "<role>",
db: "<database>"} | "<role>",
...
]
}
```
语法说明：
> user：用户
> pwd：密码
> cusomData：为任意内容，例如可以为用户全名介绍
> roles：指定用户的角色，可以用一个空数组给新用户设定空角色
> roles：可以指定内置角色和用户定义的角色

## 创建管理员用户
* 进入管理数据库
```
use amdin
```

* 创建管理用户，root权限
```
db.createUser(
    {
        user: "root",
        pwd: "root",
        roles: [ {role: "root",db: "admin"}]
    }
)
```
> 创建管理员用户的时候，必须到admin下创建，删除也是

* 查看创建完用户 后的collections
```
show tables
```

## 查看创建的管理员用户
```
show users
```

* 验证用户是否能用
```
db.auth("root","root")
# 1即为成功
```

* 在配置文件中开启用户验证
```
# 打开mongod.cfg
security:
  authorization: enabled
```
重启服务，登录测试，登录时选择admin数据库
```
# 命令行进行登录
mongo -uroot -proot admin

# 数据库中进行登录验证
use admin
db.auth("root","root")
show tables
```

## 按需求创建应用用户
* 创建对某库的只读用户
```
# 在test库，创建只读用户
use test
db.createUser(
    {
        user: "test",
        pwd: "test",
        roles: [ { role: "read",db:"test" } ]
    }
)

# 测试是否成功
db.auth("test","test")
show users

# 测试是否只读
show collections
db.createCollection('b')
```

* 创建某库的读写用户
```
db.createUser(
    {
        user: "test1",
        pwd: "test1",
        roles: [{ role: "readWrite",db: "test"}]
    }
)
```

* 创建对多库不同权限的用户
```
use app
db.createUser(
    {
        user: "app"
        pwd: "app"
        roles: [
                    { role: "readWrite",db:"app"},
                    {role: "read",db:"test"}
        ]
    }
)
```

## 删除用户
先到admin数据库
```
mongo -uroot -proot 127.0.0.1/admin
use app
db,dropUser("app")
```

---

# 库操作

## 创建数据库
```
use database_new
```
如果数据库不存在，则创建，否则切换到指定数据库
想要显示刚刚创建的数据库，需要向数据库中插入数据

## 查看所有数据库
```
show dbs
```

## 删除数据库
```
use database
db.dropDatabase()
```

---

# 表操作

## 创建表
```
db.createCollection(name,options)
```
* name：要创建的表名
* options：指定有关内存大小及索引的选项

*options参数*
 字段|类型|描述
 --|--|--|
 capped|布尔|为true，则创建固定合集（固定大小），必须指定size参数
 autoIndexld|布尔|为true，自动在`_id`字段创建索引，默认为false
 size|数值|为合集指定一个最大值
 max|数值|包含文档的最大数量

例子
```
# 创建runoob表
db.createCollection("runoob")

# 创建固定表大小
db.createCollection("runoob",{ capped:true, autoIndexId:true, size:6142800, max:10000})
```

## 删除表
```
db.collection.drop()
```

例如：删除runoob库中的表site
```
use runoob
show tables
db.site.drop()
```

## 查看表
```
show collections
```

---


# 字段与数据

## 插入数据
在MongoDB中，你不需要创建表
当你插入一些文档时，MongoDB会自动创建
可使用`save()`或`inert()`方法向集合中插入文档
```
db.tables_name.insert()
```

* 直接插入文档
```
# 例子
db.test.insert({name:'Nice',
    by: 'test'
    number: 100
})

```

* 变量形式插入
```
document=({
    by: 'test'
    number: 100
});
db.test.insert(document)
```

* 向指定表中插入一条文档数据
```
db.tables_name.insertOne()

# 例子
var document = db.test.insertOne({"a":3})
```

* 向指定表中插入多条文档数据
```
db.tables_name.inertMany()

# 例子
var document = db.test.insertOne({"a":3},{"b":4})
```

## 查看内容（文档）

### 多条件查询
* 查看集合中的所有文档
```
db.tables_name.find()
```

* 查询指定过滤条件
```
db.tables_name.find({'username':'parry'})
# SELECT * FROM inventory WHERE username="parry"
```

* 查询操作符指定条件（in）
```
# 查看test表中的name字段下是否有hello word
db.test.find({name:{$in:["hello word!"]}})
# 
SELECT * FROM inventory WHERE name in ("hello word!")
```

> 需要填写查询条件的全部字段

* 指定And条件
```
# 查询name=hello word! and age=30的内容
 db.test.find({name:"hello word!",age:30})

# SELECT * FROM inventory WHERE name=hello AND age=30
```

* 指定or条件
```
 db.test.find($or [{name:"hello word!"},{age:30}])
```

### pretty()
当数据较长的时候，会比较美观一点
```
db.runoob.find({'username':'parry'}).pretty()
```

### 正则查询
```
db.tables_name.find({字段名:{$regex:'正则规则'}})
```

### 排序
```
# 值：1位正序，-1位倒序
sort({"字段名":值})

# 例子
db.runoob.find().sort({age:-1})
```

## 更改数据
* updateOne
* updateMany
* replaceOne
* update()：用于更新已近存在的文档
```
# 语法
db.tables_name.update( <query>,<update>,
{
    upsert: <boolean>,
    multi: <boolean>,
    writeConcern: <document>
})
```
参数说明：
* query：update的查询条件，where语句
* update：update的对象和一些更新的操作符等，$set语句
* upsert：如果不存在update的计量，是否插入objNew true为插入，默认为false
* multi：默认false，只更新找到的第一条记录，为true，就把按条件查出来多条计量全部更新
* writeConcern：抛出异常的级别

例子
```
# a:3 改为 a:4
db.test.update({'a':3},{$set:{'a':4}})
```
只会修改第一条发现的文档
如需要修改多条相同的文档，则需要设置muti为true
```
db.test.update({'a':3},{$set:{'a':4}},{mulit:true})
```

```
# 只更新第一条记录

db.col.update( { "count" : { $gt : 1 } } , { $set : { "test2" : "OK"} } );
# 全部更新

db.col.update( { "count" : { $gt : 3 } } , { $set : { "test2" : "OK"} },false,true );
# 只添加第一条

db.col.update( { "count" : { $gt : 4 } } , { $set : { "test5" : "OK"} },true,false );
# 全部添加进去

db.col.update( { "count" : { $gt : 5 } } , { $set : { "test5" : "OK"} },true,true );
# 全部更新

db.col.update( { "count" : { $gt : 15 } } , { $inc : { "count" : 1} },false,true );
# 只更新第一条记录

db.col.update( { "count" : { $gt : 10 } } , { $inc : { "count" : 1} },false,false );
```

## save() 方法
通过传入的文档来替换已有文档
```
db.tables_name.save(
    <document>
    {
        writeConcern: <document>
    }
)
```
参数说明：
* document：文档数据
* writeConcern：抛出异常的级别

## 删除文档
### remove()
并不会真正的回收磁盘空间
需要继续执行`db.repairDatabase() `来释放
```
db.collection.remove(
   <query>,
   {
     justOne: <boolean>,
     writeConcern: <document>
   }
)
```
参数说明：
* query :（可选）删除的文档的条件
* justOne : （可选）如果设为 true 或 1，则只删除一个文档，如果不设置该参数，或使用默认值 false，则删除所有匹配条件的文档
* writeConcern :（可选）抛出异常的级别

删除所有数据
```
db.tables_name.remove({})
```

删除单条数据
```
# 删除a的文档
db.test.remove({'a':3})
```

### deleteOne()与deleteMany()
* 删除全部
```
db,inventory.deleteMany({})
```


* 删除status，等于A的全部文档
```
db.inventory.deleteMany({ status : "A" })
```

* 删除 status 等于 D 的一个文档
```
db.inventory.deleteOne( { status: "D" } )
```

---

# 索引

## 建立
```
db.tables_name.ensureIndex({"username",1})
```

## 查询
```
db.tables_name.getIndexes()
```

---

# 数据库的备份与恢复
* 备份
```
mongodump -h dbhost -d dbname -o dbdirectory
# host：主机名
# dbname ：库
# dbdirectory：目录
```

* 恢复
```
mongorestore -h host -d dbname --dir dbdirectory
```

# 相关链接
[官方文档](https://docs.mongodb.com/manual/reference/configuration-options/)
[菜鸟教程](http://www.runoob.com/mongodb/mongodb-tutorial.html)
还有一个链接的，突然找不到了，有时间看看补上