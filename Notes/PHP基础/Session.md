# 0x00 简介

`Session`：中文名叫 "会话" ，这里的会话是指从一个浏览器窗口打开到关闭的这个期间（特定的时间概念）

当Session与网络协议相关联时，它又往往隐含了`面向连接`和`保持状态`这样的含义。

面向连接：指在通信双方在通信之前要先建立一个通信的渠道

保持状态：指在通信的一方能够把一系列的消息关联起来，使得消息之间可以互相依赖

<!--more-->



## 工作原理

当启动一个Session会话时，会生成一个随机且唯一的Seesion_id（Session文件名）

此时Session_id存储在服务器内存中，当关闭网页时，此id会自动注销

重新登录页面，会再一次生成随机且唯一的id



---



# 0x01 创建会话

步骤：启动会话 >> 注册会话 >> 使用会话 >> 删除会话



## 启动会话

启动会话的方式有两种：Session_start()，session_register()



* session_start()

  ```php
  bool sessoin_start(); //初始化session
  ```

  > Ps：在页面开始位置调用，然后会话变量被登录到数据$_SESSION，使用之前不能有任何输出，否则会报错

* session_register()

  为会话创建一个变量来隐含地启动会话，但要求设置php.ini配置文件的选项（`register_globals=on`）

  > Ps：使用session_register()函数不在需要调用session_start()函数，PHP会在创建变量之后隐含地调用session_start()函数


## 注册会话

```php
# 通过$_SESSION注册session变量
session_start();
$_SESSION["admin"] = 'test';
echo $_SESSION["admin"];
```



## 使用会话

需要先判断一个会话ID是否存在

​	不存在则创建，并且能够通过`$_SESSION`进行访问

​	存在，则将这个会话变量载入以供用户使用

```php
session_start();
$_SESSION['admin'] = 'test';
if(!empty($_SESSION['admin'])){
    $myvalue = $_SESSION['admin'];
	echo "已添加会话";
}
```



## 删除会话

主要有3种：删除单个，删除多个，结束当前会话



* 删除单个会话

  即删除单个会话变量，和数组的操作一样，直接注销`$_SESSION`数组的某个元素

  ```php
  unset($_SESSION['admin']);
  ```

* 删除多个会话

  即一次注销所有会话变量，可以赋值空数组给`$_SESSION`

  ```php
  $_SESSION = array();
  ```

* 结束当前会话

  应该注销所有的会话变量

  ```php
  session_destroy();
  ```



---



# 0x02 Session 设置时间



## 客户端没有禁止Cookie

* session_set_cookie_params()

  Session结合Cookie设置失效时间，必须在session_start之前调用

  ```php
  $time = 1 * 60;
  sesseion_set_cookie_params($time);
  session_start();
  $_SESSION['admin'] = 'mr';
  ```

  > 不推荐使用此函数，在一些浏览器上会出现问题，所以一般手动设置失效时间

* setcookie()

  ```php
  session_start();
  $time = 1 * 60;
  setcookie('admin','test',time()+$time,'/');
  $_SESSION['admin'] = 'mr';
  ```



## 客户端禁止Cookie

当客户端禁用Cookie，Session页面间传递会失效



* 在登录之前提示用户必须打开Cookie（大多数论坛的做法）

* 设置php.ini配置文件中的`session.use_trans_sid=1`，或编译时打开`-enable-trans-sid`选项

* 通过GET方法，隐藏表单传递session_id

  ```php+HTML
  <form id="form1" name="form1" method="post" action="common.php?<?=session_name();?>=<?=session_id();?>">
      
  <?php
      $sess_name = session_name();
      $sess_id = $_GET[$sess_name];
      session_id($sess_id);
      session_start();
      $_SESSION['admin'] = 'mr';
  ?>
  ```

  > Session为请求该页面之后会产生一个session_id
  >
  > 如果这时禁止了Cookie就无法传递session_id，在请求下一个页面时将会产生一个session_id
  >
  > 这就造成了Session在页面间传递失效

* 使用文件或数据库存储Session_id，在页面间传递中手动调用



---



# 0x03 Sessio 临时文件

在服务器中，如果将所有用户的session都保存到临时目录中，会降低服务器的安全性和效率

使用`session_save_path()`解决

```php
$path = './tmp/';
session_save_path($path);
session_start();
$_SESSION['admin'] = 'mr';
```



---



# 0x04 Session 缓存

Session缓存是将网页中的内容临时存储到IE客户端的Temporary Internet Files文件夹下，并且可以设置缓存的时间

```php
# Session 缓存函数
session_cache_limiter(cache_limiter);

/*
public：响应可被任何缓存区缓存
private：对于单个用户的整个或部分响应消息，不能被共享缓存处理
nocache：清空
*/
```



设置缓存时间

```php
session_cache_expire(); // 分钟为基础
```



> Ps：这两个函数必须设置在`session_start()`之前

例子：

```php
session_cache_limiter('private');
$cache = session_cache_limiter(); //开启客户端缓存
session_cache_expire(30);
$cache_expire = session_cache_expire(); //开启客户端缓存时间
session_start();
```

