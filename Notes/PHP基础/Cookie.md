# 0x00 简介

`Cookie`：是一种在客户端浏览器端存储数据并以此来跟踪和识别用户的机制

简单的说，Cookie是Web服务器暂时存储在用户硬盘上的一个文本文件，并随后被Web浏览器读取

当用户访问网站时，网站迅速读取Cookie文件记录这位访客的特定信息，从而做出迅速的反应



**Cookie文本文件的命令格式**：

```
用户名@网站地址[数字].txt
```



> Ps：Cookie文件中的内容大多都是经过加密处理，只有符合服务器的CGI处理程序才知道它们真正的含义
>
> 每个Cookie文件都是一个简单而又普通的文本文件

<!--more-->

---



# 0x01 创建Cookie

Cookie是HTTP头部的组成部分，而头部必须在页面其他内容之前发送，因此它必须是最先输出

在创建之前，输出一个HTML标记，echo语句，甚至一个空行都会导致程序出错



```php
bool setcookie(name,value,expire,path,domain,secure);

/*
name：Cookie的变量名
value：Cookie的变量值，该值保存在客户端，不能用来保存敏感信息
expire：Cookie的失效时间，单位为秒
path：Cookie在服务端的有效路径
domain：Cookie有效的域名
secure：指明Cookie是否仅通过安全的HTTPS，值为0或1
*/
```



例子

```php
setcookie('Psycho','test',time()+3600);
# 或
setcookie("Psycho","test",time()+3600,"D:\phpStudy\PHPTutorial\WWW","sariel.top",1);
```



## 浏览器中Cookie的格式

* 客户端发送cookie时

  ```
  # 每个值都用;隔开，表示可以带多个
  Cookie: key1=value1;key2=value2
  ```
* 服务器保存Cookie时

  每个`set-Cookie`只能设置一条

  ```
  set-Cookie: key1=value1;path=/;domain=xxx
  ```



**属性**
* `Domain and path`：定义cookie的作用域
    > 当指定domain时，这个domain及其子域名都会包含这个cookie
    > path：可以访问此cookie的页面路径
* `Expires/Max-Age`：定义cookie的什么周期
* `HttpOnly`：禁用脚本访问
* `Size`：此cookie大小
* `secure`：设置是否只能通过https来传递此cookie



---



# 0x02 读取Cookie

使用超全局变量：`$_COOKIE`

```php
echo $_COOKIE['Psycho']; // test，这里的值就是我们刚刚设置的value
echo '<br />';
print_r($_COOKIE); // Array ( [Psycho] => test )
```



---



# 0x03 删除Cookie

当Cookie被创建后，如果没有设置它的失效时间，其Cookie文件会在关闭浏览器时被自动删除



* setcookie函数删除

  删除Cookie只需要将第二个参数设置为空值，第三个参数设置为小于系统当前时间

  把失效时间设置为0，也可以直接删除Cookie

  ```php
  setcookie('Psycho','',time()-1);
  ```

* 在浏览器中手动删除

  在使用Cookie时，Cookie自动生成一个文本文件存储的IE浏览器的Cookies临时文件夹中

  > 启动IE浏览器 >> 打开 Internet选项 >> 常规 >> 删除Cookies



---



# 0x04 Cookie生命周期

不设置Cookie失效时间，就表示它的生命周期就是浏览器会话期间，只要关闭浏览器Cookie就会自动销毁

这种Cookie一般不保存在硬盘上，而是保存在内存中



设置了失效时间，那么浏览器会把Cookie保存在硬盘中，再次打开IE浏览器时会依然有效



虽然Cookie可以长期保存在客户端浏览器中，但是也不是一成不变的

因为浏览器最多允许存储300个Cookie文件，而每个Cookie文件支持最大容量为4KB，每个域名最多支持20个Cookie，如果达到限制，会自动随机地删除Cookie文件