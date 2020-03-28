# 简介
`PDO`：PHP数据对象简称，只需要使用PDO接口中的方法就可以对数据库进行操作，在选择不同的数据库时，只需修改PDO和DSN（数据源名称）
PHP6中默认使用PDO连接数据库，非PDO扩展将会在PHP6中被移除
**特点**：

* 让跨数据库的使用更具亲和力，与ADODB和MDB2相比，PDO更高效
* PDO扩展是模块化的，能够在运行时为数据库后端加载驱动程序，而不必重新编译或重新安装整个PHP程序
* 轻松地与各种数据库进行交互
* 实现PHP脚本最大限度抽象性和兼容性

<!--more-->

---


# 安装PDO
由于PDO需要PHP5核心面向对象特性的支持，因此其无法再PHP5之前的版本中使用
默认：PHP5.2开启，但是要启动某个数据库驱动程序的支持，仍需要进行相应的配置操作
**Linux**：在`configure`命令中添加如下选项
```
--with-pdo-mysql=/path/to/mysql/installation
```
**windows**：在`php.ini`配置文件中进行设置
```
extension=php_pdo.dll
;extension=php_pdo_firebird.dll
extension=php_pdo_mssql.dll
extension=php_pdo_mysql.dll
extension=php_pdo_oci.dll
extension=php_pdo_oci8.dll
extension=php_pdo_odbc.dll
;extension=php_pdo_pgsql.dll
extension=php_pdo_sqlite.dll
```
> 启动PDO，首先必须加载`extension=php_pdo.dll`
> 支持某个具体的数据库，加载对应的数据库选项：`extension=php_pdo_mysql.dll`（mysql）
> 保存php.ini配置文件，并重启Apache服务器，才能生效

---

# DSN
`DSN`：数据库源的缩写，提供连接数据库所需要得信息
PDO的DSN包括3个部分：
* PDO驱动名称（数据库）
* 冒号
* 驱动特定的语法

在使用不同的数据库时，必须明确数据库服务器是完全独立于PHP的实体
由于数据库服务器只在特定的端口上监听连接请求，每种数据库服务器具有一个默认的端口号
但是数据库管理员可以对端口号进行修改，所以PHP有可能找不到数据库的端口，此时就可以在DSN中包含端口号
在通过DSN连接数据库时，通常都包括数据库名称，这样可以确保连接的的是想要的数据库

---

# 连接数据库
在PDO中，要建立与数据库的连接需要实例化PDO的构造函数
```php
__construct($dsn[,$username[,$password[,array $driver_options]]]);
/*
dsn：数据库名
username：用户
password：密码
driver_options：连接数据库的其他选项
*/
```
不管使用哪种驱动程序，都是用PDO类名
> PS：如果有任何连接错误，将抛出一个PDOException异常对象

```php
$dbms='mysql'; //数据库类型
$host='localhost'; // 数据库主机名
$dbName = 'test'; // 数据库名
$user = 'root'; // 用户名
$pass = ''; // 密码
$dsn = "$dbms:host=$host;dbname=$dbName";

try{
    $dbn = new PDO($dsn,$user,$pass); // 初始化一个PDO对象
    echo '连接成功';
    $dbh = null;
}catch(PDOException $e){
    die("Error! : ".$e->getMessage()."<br />");
}
// 默认这个不是长连接，如果需要数据库长连接，需要最后加一个参数
// array(PDO::ATTR_PERSISTENT => true);
// $db = new PDO($dsn,$user,$pass,array(PDO::ATTR_PERSISTENT => true));
```



## 字符串形式

```php
mysql:host=localhost;dbname=bingbing;charset=utf-8;
```

```php
$dsn = 'mysql:host=localhost;dbname=typecho;';
try{
    $pdo = new PDO($dsn,'root','');
}catch(PDOException $e){
    die($e->getMessage());
}

var_dump($pdo);
```



## 文件形式

```php
$pdo = new PDO('uri:file:///C:/wamp64/www/1604/day14/dsn.txt','root','123456');
```



## PHP.ini

```php
pdo.dsn.lala="mysql:host=localhost;dbname=bingbing;charset=utf-8"
$pdo = new PDO('lala','root','123456');
```

---



# 设置错误模式

**一般设置成第三种，抛出异常给用户看的**

* PDO::ERRMODE_SILENT（静默模式）

  > 默认模式，只简单地设置错误码
  > 如果错误时由于语句对象的调用而产生的，那么可以调用那个对象的PDOStatement::errorCode()或PDOStatement::errorInfo() 方法
  > 如果错误时由于调用数据库对象产生的，可使用 PDO::errorCode() 和 PDO::errorInfo() 方法来检查语句和数据库对象

* PDO::ERRMODE_WARNING（警告模式）

  > PHP会产生`E_WARNING `信息，并设置errorCode属性
  > 除非明确地检查错误代码，否则程序将继续运行
  > 如果只是想看看发生了什么问题且不中断应用程序的流程，那么此设置在调试/测试期间非常有用

* PDO::ERRMODE_EXCEPTION（异常模式）

  > 除了设置错误码之外，PDO还将抛出一个PDOException异常类
  > 并设置它的属性来反射错误码和错误信息

| 方法               | 描述                                   |
| ------------------ | -------------------------------------- |
| getMessage()       | 取得文本化的错误信息                   |
| getCode()          | 取得 SQLSTATE 错误代号                 |
| getFile()          | 取得发生异常的文件名                   |
| getLine()          | 取得 PHP 程序产生异常的代码所在行号    |
| getTrace()         | backtrace() 数组                       |
| getTraceAsString() | 取得已格成化成字符串的 getTrace() 信息 |

**设置错误模式**

```php
$pdo -> setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_WARNING); // 警告模式
$pdo -> setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION); // 异常模式
```



例子

```php
$dsn = 'mysql:dbname=testdb;host=127.0.0.1';
$user = 'dbuser';
$password = 'dbpass';

try {
    $dbh = new PDO($dsn, $user, $password);
    $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // 设置成异常模式
} catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
}
```

> Ps：不管当前是否设置了 PDO::ATTR_ERRMODE 
>
> 如果连接失败，PDO::__construct() 将总是抛出一个 PDOException 异常。未捕获异常是致命的



在构造函数中设置错误模式

```php
$dsn = 'mysql:dbname=test;host=127.0.0.1';
$user = 'googleguy';
$password = 'googleguy';

/*
    使用 try/catch 围绕构造函数仍然有效，即使设置了 ERRMODE 为 WARNING，
    因为如果连接失败，PDO::__construct 将总是抛出一个  PDOException 异常。
*/
try {
    $dbh = new PDO($dsn, $user, $password, array(PDO::ATTR_ERRMODE => PDO::ERRMODE_WARNING));
} catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
    exit;
}

// 这里将导致 PDO 抛出一个 E_WARNING 级别的错误，而不是 一个异常 （当数据表不存在时）
$dbh->query("SELECT wrongcolumn FROM wrongtable");
```

---



# 错误处理

* `errorCode()`：用于获取在操作数据库句柄时所发生的错误代码

  这些错误代码被称为SQLSTATE代码

  `SQLSTATE`：5个数字和字母组成的代码

  ```php
  PDOStatement::errorCode(void);
  // 返回SQLSTATE
  
  # 例子
  /* 引发一个错误 -- BONES 数据表不存在 */
  $dbh->exec("INSERT INTO bones(skull) VALUES ('lucy')");
  
  echo "\nPDO::errorCode(): ";
  print $dbh->errorCode(); //PDO::errorCode(): 42S02
  ```

* `errorInfo()`：返回最后一次操作数据库的错误信息描述‘

  ```php
  public array PDO::errorInfo ( void );
  /*
  0：SQLSTATE 错误码 (5个字母或数字组成的在 ANSI SQL 标准中定义的标识符).
  1：错误代码
  2：错误信息
  */
  
  # 例子
  /* 错误的SQL语法 */
  $stmt = $dbh->prepare('bogus sql');
  if (!$stmt) {
      echo "\nPDO::errorInfo():\n";
      print_r($dbh->errorInfo());
  }
  ```

  > Ps：如果数据库句柄没有进行操作，则返回 NULL

---



# 执行Sql语句

* exec

  ```
  PDO::exec(statement);
  /*
  startement：Sql执行语句
  主要执行不要结果集的语句，增删改
  返回执行查询时受影响的行数
  */
  ```

  ```php
  $dsn = 'mysql:host=localhost;dbname=dan;';
  
  try {
      $pdo = new PDO($dsn, 'root', 'root');
  	// 设置错误模式
      $pdo->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
  } catch (PDOException $e) {
      die('数据了连接失败：' . $e->getMessage());
  }
  
  try {
      $sql = "insert into user(username,password) values('php','523')";
      $ret = $pdo->exec($sql);
      echo "数据添加成功，受影响行数为： " . $res;
  } catch (Exception $e){
      die("Error：".$e->getMessage().'<br />');
  }
  ```

* query

  ```
  PDO::query(statement);
  // 进行要结果集的语句，查，desc
  ```

  ```php
  $dsn = 'mysql:host=localhost;dbname=dan;';
  
  try {
      $pdo = new PDO($dsn, 'root', 'root');
  	// 设置错误模式
      $pdo->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
  } catch (PDOException $e) {
      die('数据了连接失败：' . $e->getMessage());
  }
  
  try {
      $sql = "select * from user";
      $ret = $pdo->query($sql);
      print_r($res);
  } catch (Exception $e){
      die("Error：".$e->getMessage().'<br />');
  }
  ```

`lastInsertId`：用于最后插入语句的ID号

---



# 预处理语句

优点：效率，安全（SQL注入）

```php
PDOStatement
prepare();       预处理sql语句
execute();        执行sql语句
```

**绑定变量**：`bindParam`，在执行预处理之前，将之前预处理语句指定的变量进行赋值

只能通过变量的形式进行赋值（引用传值）

```php
$stmt = $pdo -> prepare('insert in to user(name) values(?)');
$stmt -> bindParam("占位符/命名参数"，$变量名);
$变量名 = '111'；
```



## 详解

```php
PDO::prepare ( string $statement [, array $driver_options = array() ] );
/*
statement：合法的SQL语句
driver_options：此数组包含一个或多个 key=>value 对来设置 PDOStatement 对象的属性， 最常使用到是将PDO::ATTR_CURSOR值设置为PDO::CUR
SOR_SCROLL：请求一个可滚动游标
*/
```

* 使用`?`占位符

  ```php
   $stmt = $pdo -> prepare('insert in to user(name,password,money) values(?,?,?)');
   $stmt -> bindParam(1,$name);
   $stmt -> bindParam(2,$pwd);
   $stmt -> bindParam(3,$money);
   $name = 'xxx';
   $pwd = '123456789';
   $money = 3000;
  ```

* 使用命名参数（:参数名）

  ```php
   $stmt = $pdo -> prepare('insert in to user(name,password,money) values(:name,:password,:money)');
   $stmt -> bindParam(':name',$name);
   $stmt -> bindParam(':password',$pwd);
   $stmt -> bindParam(':money',$money);
   $name = 'xxx';
   $pwd = '123456789';
   $money = 3000;
  ```

  



例子1：命名参数

```php
$dsn = 'mysql:host=localhost;dbname=dan;';
try {
    $pdo = new PDO($dsn, 'root', 'root');
    //设置错误模式
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('数据库链接失败' . $e->getMessage());
}
try {
    //预处理
    $stmt = $pdo->prepare('insert in to user(name,password,money) values(:name,:password,:money)');
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':password', $pwd);
    $stmt->bindParam(':money', $money);
    /*设置值并执行语句*/
    $name = 'xxx';
    $pwd = '123456789';
    $money = 3000;
    $stmt->execute();
    /* 再次设置值并执行语句*/
    $name = 'sss';
    $pwd = '123456789';
    $money = 3000;
    $stmt->execute();
} catch (PDOException $e) {
    echo $e->getMessage();
}
```



例子2：使用`?`占位符

```php
dsn = 'mysql:host=localhost;dbname=dan;';
try {
    $pdo = new PDO($dsn, 'root', 'root');
    //设置错误模式
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('数据库链接失败' . $e->getMessage());
}
try {
    //预处理
    $stmt = $pdo->prepare('insert in to user(name,password,money) values(?,?,?)');
    $stmt->bindParam(1, $name);
    $stmt->bindParam(2, $pwd);
    $stmt->bindParam(3, $money);
    $name = 'xxx';
    $pwd = '123456789';
    $money = 3000;
    $stmt->execute();
    $name = 'sss';
    $pwd = '123456789';
    $money = 3000;
    $stmt->execute();
} catch (PDOException $e) {
    echo $e->getMessage();
}
```



例子3 ：命名参数下，使用关联数组

```php
$dsn = 'mysql:host=localhost;dbname=dan;';
try {
    $pdo = new PDO($dsn, 'root', 'root');
    //设置错误模式
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('数据库链接失败' . $e->getMessage());
}
try {
    //预处理
    $stmt = $pdo->prepare('insert in to user(name,password,money) values(:name,:password,:money)');
    //占位符的情况下，使用关联数组
    $stmt->execute([':name' => '刘备', ':password' => '123', ':money' => 1000]);
} catch (PDOException $e) {
    echo $e->getMessage();
}
```



例子4：占位符下，使用索引数组

```php
$dsn = 'mysql:host=localhost;dbname=dan;';
try {
    $pdo = new PDO($dsn, 'root', 'root');
    //设置错误模式
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('数据库链接失败' . $e->getMessage());
}
try {
    //预处理
    $stmt = $pdo->prepare('insert in to user(name,password,money) values(?,?,?)');
    //?情况下,使用索引数组
    $stmt->execute(['xx', '789456123', '1555']);
} catch (PDOException $e) {
    echo $e->getMessage();
}
```



例子5

```php
$dsn = 'mysql:host=localhost;dbname=dan;';
try {
    $pdo = new PDO($dsn, 'root', 'root');
    //设置错误模式
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die('数据库链接失败' . $e->getMessage());
}
try {
    //预处理
    $stmt = $pdo->prepare('delect from user where id=?');
    $stet->execute([1]);
    //?情况下,使用索引数组
    $stmt->execute(['xx', '789456123', '1555']);
} catch (PDOException $e) {
    echo $e->getMessage();
}
```

---



# 事物处理

`事务`：若干事件的集合

`事务处理`：当所有事件执行成功，事务才执行，若有任何一个事件不能成功执行，事务的其他事件也不被执行

事物处理的四大特性：

* 原子性
* 一致性
* 隔离性
* 持久性

> Ps：表引擎有两种`myisam`（不支持），`innodb`（支持）

```
$pdo -> beginTransaction(); // 开启一个事物
$pdo -> commit(); // 提交事物
$pdo -> rollback(); // 回滚到初始状态
```

例子

```php
$dsn = 'mysql:host=localhost;dbname=dan;';
try{
    $pdo = new PDO($dsn,'root','root');
    //设置错误模式
    $pdo -> setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
}catch (PDOException $e){
    die('数据库链接失败'.$e->getMessage());
}
try{
 //开启一个事物
    $pdo -> beginTransaction();
    $sql = 'update user set monney=money-500 where id=1';
    $ret = $pdo -> exec($sql);
    if ($ret > 0){
        echo '导出成功<br />';
    }else{
        echo '导出失败<br />';
        throw new PDOException('失败');
    }
}catch (PDOException $e){
    $pdo -> rollback();
    echo $e -> getMessage();
}
```

> Ps：一般事务处理是运行在`try-catch`语句中

---



# 查看结果

* `fetch()`：从结果集中获取下一行

  ```php
  PDOStatement::fetch ();
  /*
  PDO::FETCH_ASSOC：返回一个索引为结果集列名的数组
  PDO::FETCH_BOTH（默认）：返回一个索引为结果集列名和以0开始的列号的数组
  PDO::FETCH_BOUND：返回 TRUE ，并分配结果集中的列值给PDOStatement::bindColumn() 方法绑定的 PHP 变量
  PDO::FETCH_CLASS：返回一个请求类的新实例，映射结果集中的列名到类中对应的属性名
  PDO::FETCH_INTO：更新一个被请求类已存在的实例，映射结果集中的列到类中命名的属性
  PDO::FETCH_LAZY：结合使用 PDO::FETCH_BOTH 和 PDO::FETCH_OBJ，创建供用来访问的对象变量名
  PDO::FETCH_NUM：返回一个索引为以0开始的结果集列号的数组
  PDO::FETCH_OBJ：返回一个属性名对应结果集列名的匿名对象
  */
  
  # 例子
  $sth = $dbh->prepare("SELECT name, colour FROM fruit");
  $sth->execute();
  
  /* 运用 PDOStatement::fetch 风格 */
  print("PDO::FETCH_ASSOC: ");
  print("Return next row as an array indexed by column name\n");
  $result = $sth->fetch(PDO::FETCH_ASSOC);
  print_r($result);
  print("\n");
  ```

* `fetchAll()`：返回一个包含结果集中所有行的数组

  ```php
  PDOStatement::fetchAll ([ int $fetch_style [, mixed $fetch_argument [, array $ctor_args = array() ]]] );
  /*
  fetch_style：控制下一行如何返回给调用者
  	想要返回一个包含结果集中单独一列所有值的数组，需要指定 PDO::FETCH_COLUMN
  	想要获取结果集中单独一列的唯一值，需要将 PDO::FETCH_COLUMN 和 PDO::FETCH_UNIQUE 按位或
  	想要返回一个根据指定列把值分组后的关联数组，需要将 PDO::FETCH_COLUMN 和 PDO::FETCH_GROUP 按位或
  fetch_argument：
  	PDO::FETCH_COLUMN：返回指定以0开始索引的列
  	PDO::FETCH_CLASS：返回指定类的实例，映射每行的列到类中对应的属性名
  	PDO::FETCH_FUNC：将每行的列作为参数传递给指定的函数，并返回调用函数后的结果
  ctor_args：当 fetch_style 参数为 PDO::FETCH_CLASS 时，自定义类的构造函数的参数
  */
      
  # 例子
  $sth = $dbh->prepare("SELECT name, colour FROM fruit");
  $sth->execute();
  
  /* 获取结果集中所有剩余的行 */
  print("Fetch all of the remaining rows in the result set:\n");
  $result = $sth->fetchAll();
  print_r($result);
  
  /* 获取第一列所有值 */
  $result = $sth->fetchAll(PDO::FETCH_COLUMN, 0);
  var_dump($result);
  ```

* `setFetchMode`：设置默认的提取模式

  ```php
  PDOStatement::setFetchMode ( int $PDO::FETCH_CLASS , string $classname , array $ctorargs );
  /*
  mode：获取模式必须是 PDO::FETCH_* 系列常量中的一个
  colno：列号
  classname：类名
  ctorargs：构造函数参数
  object：对象
  */
  
  # 例子
  $sql = 'SELECT name, colour, calories FROM fruit';
  try {
    $stmt = $dbh->query($sql);
    $result = $stmt->setFetchMode(PDO::FETCH_NUM);
    while ($row = $stmt->fetch()) {
      print $row[0] . "\t" . $row[1] . "\t" . $row[2] . "\n";
    }
  }
  catch (PDOException $e) {
    print $e->getMessage();
  }
  ```

* `bindColumn()`：绑定一个列到PHP变量

  把结果集输出到绑定的PHP变量中

  ```php
  PDOStatement::bindColumn ( mixed $column , mixed &$param [, int $type [, int $maxlen [, mixed $driverdata ]]] );
  /*
  column：结果集中的列号（从1开始索引）或列名。如果使用列名，注意名称应该与由驱动返回的列名大小写保持一致
  param：将绑定到列的 PHP 变量名
  type：通过 PDO::PARAM_* 常量指定的参数的数据类型
  maxlen：预分配提示
  driverdata：驱动的可选参数
  */
  
  //$stmt -> bindColumn('name',$name);
  //$stmt -> fetch(PDO::FETCH_NUM);
  
  # 例子
  function readData($dbh) {
    $sql = 'SELECT name, colour, calories FROM fruit';
    try {
      $stmt = $dbh->prepare($sql);
      $stmt->execute();
  
      /*  通过列号绑定  */
      $stmt->bindColumn(1, $name);
      $stmt->bindColumn(2, $colour);
      
      /*  通过列名绑定  */
      $stmt->bindColumn('calories', $cals);
  
      while ($row = $stmt->fetch(PDO::FETCH_BOUND)) {
        $data = $name . "\t" . $colour . "\t" . $cals . "\n";
        print $data;
      }
    }
    catch (PDOException $e) {
      print $e->getMessage();
    }
  }
  readData($dbh);
  ```



## 例子

例子1：

```php
$dsn = 'mysql:host=localhost;dbname=dan;';
try{
    $pdo = new PDO($dsn,'root','root');
    //设置错误模式
    $pdo -> setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
}catch (PDOException $e){
    die('数据库链接失败'.$e->getMessage());
}
try{
 //预处理
 $stmt = $pdo -> prepare('delect from user where id=?');
 $stet -> execute();
 $result = $stmt -> fetch(PDO::FETCH_NUM);
 var_dump($result);
}catch (PDOException $e){
 echo $e -> getMessage();
}
```



例子2：

```php
$dsn = 'mysql:host=localhost;dbname=dan;';
try{
    $pdo = new PDO($dsn,'root','root');
    //设置错误模式
    $pdo -> setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
    //设置默认提取模式
    $pdo -> setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE,PDO::FETCH_ASSOC);
}catch (PDOException $e){
    die('数据库链接失败'.$e->getMessage());
}
try{
 $stmt = $pdo -> prepare('delect from user where id=?');
 $stet -> execute();
 $result = $stmt -> fetch();
 var_dump($result);
}catch (PDOException $e){
 echo $e -> getMessage();
}
```



例子3

```php
$dsn = 'mysql:host=localhost;dbname=dan;';
try{
    $pdo = new PDO($dsn,'root','root');
    //设置错误模式
    $pdo -> setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
    //设置默认提取模式
    $pdo -> setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE,PDO::FETCH_ASSOC);
}catch (PDOException $e){
    die('数据库链接失败'.$e->getMessage());
}
try{
 $stmt = $pdo -> prepare('delect from user where id=?');
 $stet -> execute();
 $result = $stmt -> fetchAll();
 var_dump($result);
}catch (PDOException $e){
 echo $e -> getMessage();
}
```



例子4

```php
$dsn = 'mysql:host=localhost;dbname=dan';
try{
    $pdo = new PDO($dsn,'root','root');
    //设置错误模式
    $pdo -> setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
    //设置默认提取模式
    $pdo -> setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE,PDO::FETCH_ASSOC);
}catch (PDOException $e){
    die('数据库链接失败'.$e->getMessage());
}
try{
 $stmt = $pdo -> prepare('select id,username,password from user');
 $stet -> execute();
 $stmt -> bindColumn('id',$id);
 $stmt -> bindColumn('username',$usernam);
 $stmt -> bindColumn('password',$password);
 echo '<table border="1" width="800" align="center">';
 while ($stmt -> fetchAll()){
  echo '<tr>';
  echo '<td>'.$id.'</td>';
  echo '<td>'.$password.'</td>';
  echo '</tr>';
 }
 echo '</table>';
}catch (PDOException $e){
 echo $e -> getMessage();
}
```

