## 声明
转载自黑马视频中的笔记和玄魂公众号！

---


## 0x01 用户和权限的基本概念

### 基本概念
* <b>用户</b>是Linux系统工作中重要的一环，用户管理包括<b>用户</b>与<b>组</b>
* 在Linux系统中，不论是由本级或是远程登录系统，每个系统都<b>必须拥有一个账号</b>，并且<b>对于不同的系统资源拥有不同的使用权限</b>
* 对<b>文件/目录</b>的权限包括：

|序号|权限|英文|缩写|数字代号|
|:--:|:--:|:--:|:--:|:--:|
|01|读|read|r|4|
|02|写|write|w|2|
|03|执行|excute|x|1|
|04|无权限||-|0|

<!--more-->

### 组
为了方便用户管理，提出组的概念
* 在实际应用中，可以预先针对**组**设置好权限，然后**将不同的用户添加到对应的组中**，从而**不用依次为每一个用户设置权限**

### ls -l扩展
`ls -l` 可以查看文件夹下文件的详细信息

从左到右依次是：
* **权限**，第一个字符，如果是d表示目录
* **硬链接数**，通俗地讲，就是有多少种方式，可以访问到当前目录/文件
* **拥有者**，家目录下 文件/目录 的拥有者通常都是当前用户
* **组**，在Linux中，很多时候，会出现组和用户名相同的情况
* **大小**
* **时间**
* **名称**

### 超级用户
* 在Linux系统中的`root`账号通常 **用于系统的维护和管理**，对操作系统的所有资源**具有所有访问权限**
* 在大多数版本的Linux中，都不推荐**直接使用root账号登录系统**
* 在Linux安装的过程中，系统会自动创建一个用户账号，而这个默认的用户就称为"标准用户"

#### sudo
* `su`表示**使用另一个用户的身份**
* `sudo`命令用来其他身份来执行命令，预设的身份为`root`
* 用户使用`sudo`时，必须先输入密码，之后有**5分钟的有效期限**，超过期限则必须重新输入密码
> 若其未经授权的用户企图使用`sudo`，则会发出警告邮件给管理员


---

## 0x02 组管理
> 提示：创建组/删除组 的终端命令都需要通过`sudo`执行

|序号|命令|作用|
|:--:|--|--|
|01|groupadd组名|添加组|
|02|groupdel组名|删除组|
|03|cat /etc/group|确认组信息|
|04|chgrp -R 组名 文件/目录名|修改文件/目录的所属组|

> 提示：
* 组信息保存在 `/etc/group`文件中
* `/etc`目录是专门用来保存**系统配置信息**的目录
* 在实际应用中，可以预先针对组设置好权限，然后**将不同的用户添加到对应的组中**，从而**不用依次为每一个用户设置权限**


---

## 0x03 用户管理 的终端命令
> 提示：**创建用户/删除用户/修改其他用户密码**的终端命令都需要通过`sudo`执行

|序号|命令|作用|说明|
|:--:|--|--|--|
|01|useradd -m -g 组新建用户名|添加新用户|**-m**自动建立用户家目录。**-g**指定用户所在的组，否则会建立一个和同名的组|
|02|passwd 用户名|设置用户密码|如果是普通用户直接passwd可以修改自己的账户密码|
|03|userdel -r 用户名|删除用户|**-r**选项会自动删除用户家目录|
|04|cat /etc/passwd | grep |确认用户信息,新建用户后，用户信息胡保存在/etc/passwd文件中|

### useradd
用来建立用户账号和创建目录的起始目录
```
useradd [option] name
```
|参数|含义|
|:--:|--|
|-G group|定义此使用为一堆groups的成员|
|-m|使用者目录如不存在则自动建立|
|-M|不建立使用者目录|
|-n|预设值使用者群主与使用者名称会相同，此选项将取消此预设值|
|-r|用来建立系统账号|
|-s shell|使用者登入后使用者的shell名称|
|-u uid|使用者的ID值|
|||
|可选选项||
|-b default_home|定义使用者所属目录的前一个目录|
|-e default_expire_date|使用者账号停止日期|
|-f default_inactive|账号过期几日后停权|
|-g default_group|新账号起始群组名或ID|
|-s default_shell|使用者登入后使用的shell名称|

提示：
* 创建用户时，如果忘记添加`-m`选项指定新用户的家目录，删除用户，重新创建


### passwd
设置用户密码的
```
passwd [option] username
```
|参数|含义|
|:--:|--|
|-k|保留未过期的身份验证令牌|
|-l|关闭账号密码，效果相当于usermod -L|
|-u|修复账号密码，效果相当于usermod -U|
|-g|修改组密码，gpasswd的等效命令|
|-f|更改由finger命令访问的用户信息|
|-d|关闭使用者的密码认证功能，使用者在登入时将可以不用输出密码|
|-S|显示指定使用者的密码认证种类|

```
# 设置一个用户的密码
passed root

# 消除一个用户的密码
passwd -d root

# 查询用户的密码状态 
passwd -S root
```
> 提示：执行完passwd -d 之后这个用户模式是Empty password


### userdel
删除指定的用户
若不加选项，则仅删除用户账户，而不删除相关文件
```
userdel [option] username
```
|参数|含义|
|:--:|--|
|-f|强制删除用户，即使用户当前已登录|
|-r|删除用户的同时，删除与用户相关的所有文件|

常见用法：
* 删除一个用户，不删除相关文件
```
userdel rooot
```
* 被人植入后门账户，正在有人登陆，可以进行强制删除并删除文件夹
```
userdel -rf rooot
```

---

## 0x04 查看用户信息
|序号|命令|作用|
|:--:|--|--|
|01|id [用户名]|查看用户UID和GID信息|
|02|who|查看当前所有登录的用户列表|
|03|whoami|查看当前登录用户的账户名|

### passwd文件
`/etc/passwd`文件存放的是用户的信息，由6个分号组成的7个信息
1.**用户名**
2.**密码（x，表示加密的密码）**
3.**UID（用户标识）**
4.**GID（组标识）**
5.**用户全名或本地账号**
6.**家目录**
7.**登录使用的Shell，就是登录之后，使用的终端命令，`ubantu`默认是`dash`**


### usermod
* `usermod`可以用来设置**用户**的**主组/附加组**和**登录shell**，修改用户的信息
* **主组**：通常在新建用户时指定，在`etc/passwd`的第四列**GID对应的组**
* **附加组**：在`/etc/group`中最后一列表示该组的用户列表，用于指定**用户的附加权限**

> 提示：设置了用户的附加组之后，需要重新登录才能生效

```
usermod [option] name
```
> 注意：默认使用`useradd`添加的用户是没有权限使用`sudo`以及`root`身份执行命令的

|序号|命令|作用|
|:--:|--|--|
|-c|修改用户账户的备注文字|
|-d|修改用户登入时的目录|
|-e|修改账号的有效期限|
|-f|修改在密码过期后多少天即关闭该账号|
|-g|修改用户所属的群组|
|-G|修改用户所属的附加群组|
|-l|修改用户账户名称|
|-L|锁定用户密码，是密码无效|
|-s|修改用户登入后所使用的shell|
|-u|修改用户ID|
|-U|解除密码锁定|

常用命令：
* 将用户添加到`sudo`附加组中
```
usermod -G sudo 用户
```
* 修改用户的主组（passwd 中的 GID）
```
usermod -g 组 用户名
```
* 修改用户的附加组
```
usermod -G 组 用户名
```
* 修改用户登录 Shell
```
usermod -s /bin/bash 用户名
```

---

### which
> 提示
* /etc/passwd  用于保存用户信息的文件
* /usr/bin/passwd  用于修改用户密码的程序
>

* `which`命令可以查看执行命令所在位置
```
which ls

# 输出
# /bin/ls

which useradd

# 输出
# /usr/sbin/useradd
```

### `bin`和`sbin`
* 在Linux中，绝大数可执行文件都是保存在`/bin`，`/sbin`，`/usr/bin`，`/usr/sbin`
* `/bin`是二进制执行文件目录，主要用于具体应用
* `/sbin`是系统管理员专用的二进制代码存放目录，主要用于系统管理
* `/usr/bin`后期安装的一些软件
* `/usr/sbin`超级用户的一些管理程序

> 提示
* `cd`这个终端命令是内置在系统内核中的，没有独立的文件，因此用`which`无法找到


---

## 0x04 切换用户

### su
切换当前用户身份到其他用户身份
```
su [option] name
```
|参数|含义|
|:--:|--|
|-c|窒息完指定的指令后，即恢复原来的身份|
|-f|适用于csh与tsch，是shell不用去读取启动文件|
|-l|改变身份时，也同时变更工作目录，以及HOME,SHELL,USER,logname|
|-s|指定要执行的shell|
|--version|显示版本信息|

常用命令：
* 切换用户到root
```
su root
```
* 只想某个用户执行一个命令之后退出
```
su -c ls test
```


### exit
退出当前登录账户
```
exit
```

---

## 0x05 修改文件权限

### chown
将指定文件的拥有者改为指定的用户或组，用户可以是`用户名`或者`用户ID`
组可以是`组名`或者`组ID`
```
chown [options] mode files

# 修改文件|目录的拥有者
chown 用户名 文件名|目录名
```
|参数|含义|
|:--:|--|
|-c|类似“-v”参数，但仅回报更改的部分|
|-f，--quite，--silent|不显示报错信息|
|-h|只对符号连接的文件作修改，而不更改其他任何相关文件|
|-R|递归处理，将制定目录下的所有文件及子目录一并处理|
|-v|显示指令执行过程|

常用命令：
* 我们用root用户在服务器上创建了一个文件，但是这个文件是要给`nginx`来使用的，所以他的`拥有者`和`组`必须是`nginx`
```
# 因为`root`的权限太高了，`nginx`对这个文件的访问会被系统拒绝，我们这样做
chown nginx:nginx nginx.conf
```
* .然后我们开始搭建网站，发现网站的`/var/www/html`下的文件都是root的，但是这些文件打算给`nginx`来使用，作为网站的根目录，怎么办
```
chown -R nginx:nginx /var/www/html
```
* 或者我们只打算改变这个文件的组
```
chown :nginx index.html
```

### chgrp
用来改变文件或目录所属的用户组
```
chgrp [option] [参数]

# 递归修改文件|目录的组
chgrp -R 组名 文件名|目录名
```
参数和chown差不多


### chmod
修改权限
> 提示：`chmod`在设置权限时，可以简单地使用三个数字分别对应**拥有者/组**和**其他**用户的权限
```
chmod [options] mode files

# 直接修改文件|目录的 读|写|执行 权限，但是不能精确到 拥有者|组|其他
chmod +/-rwx 文件名/目录名

# 递归修改文件权限
chmod -R 775 文件名|目录名
```
> 提示：以上方式会一次性修改`拥有者/组`权限

|参数|含义|
|:--:|--|
|-c|当发生改变时，报告处理信息|
|-f|错误信息不输出|
|-R|处理指定目录以及其子目录下的所有文件|
|-v|运行时显示详细处理信息|

>

|权限|含义|
|:--:|--|
|r|读权限，用数字4表示|
|w|写权限，用数字2表示|
|x|执行权限，用数字1表示|
|-| 删除权限，用数字0表示|
|s|特殊权限 |

>

|其他|含义|
|:--:|--|
|u|目录或者文件的当前的用户|
|g|目录或者文件的当前的群组|
|o|除了目录或者文件的当前用户或群组之外的用户或者群组|
|a|所有的用户及群组|

**拥有者**

|r|w|x|
|--|--|--|
|4|2|1|

**组**

|r|w|x|
|--|--|--|
|4|2|1|

**其他**

|r|w|x|
|--|--|--|
|4|2|1|

常用数组组合有（`u`表示用户/`g`表示组/`o`表示其他）
* `777` ===> `u=rwx,g=rwx,o=rwx`
* `755` ===> `u=rwx,g=rx,o=rx`
* `644` ===> `u=rx,g=r,p=r`

常用方式：
* 指定的文件`所有用户组`增加可执行的权限
```
chmod a+x database.php
```
* 后来我们发现是`apache`这个用户组没有可执行权限，为了安全考虑，其他用户组没必要具有可执行权限，我们可以这样操作
```
chmod ug+w,o-x database.php
```
> 文件属主(u)增加执行权限
> 与文件属主同组用户(g)增加执行权限
>  其他用户(o)删除执行权限

* 我们有一天发现了某个文件夹内的文件都需要一个可写的权限，比如缓存目录，我们可以这样为整个目录增加权限
```
chmod -R u+w cache/
```

