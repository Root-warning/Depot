# 简介
os模块是与操作系统交互的一个接口
经常用于对文件操作

<!--more-->

---

# 常用方法

## 当前路径及路径下的文件
* os.getcwd()
> 查看当前所在路径
* os.listdir(path)
> 列举目录下的所有文件，`返回的是列表类型`
> 包括隐藏文件


## 绝对路径和判断
* os.path.abspath(path)
> 返回path的绝对路径

* os.path.isabs(path)
> 如果path是绝对路径，返回True


## 查看路径的文件夹部分和文件名部分

* os.path.split(path)
> 将路径分解为(文件夹,文件名)，`返回的是元组类型`

* os.path.join(path1,path2...)
> os.path.join(path,name)
> 将path进行组合，若其中有绝对路径，则之前的path将被删除

* os.path.dirname(path)
> 返回path中的文件夹部分，结果不包含'\'

* os.path.basename(path)
> 返回path中的文件名


## 查看文件时间
* os.path.getmtime(path)
> 文件或文件夹的最后修改时间，从新纪元到访问时的秒数

* os.path.getatime(path)
> 文件或文件夹的最后访问时间，从新纪元到访问时的秒数

* os.path.getctime(path)
>文件或文件夹的创建时间，从新纪元到访问时的秒数


## 查看文件大小
* os.path.getsize(path)
> 文件或文件夹的大小，若是文件夹返回0


## 查看文件是否存在
* os.path.exists(path)
> 文件或文件夹是否存在，返回True 或 False


## 一些表现形式参数
os中定义了一组文件，路径在不同操作系统中的表现形式参数
* os.sep
> 显示当前平台下路径分隔符

* os.linesep
> 给出当前平台使用的行终止符

* os.pathsep
> 输出用于分割文件路径的字符串

* os.name
> 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'


---

# 目录与文件操作相关

## 生成目录
* os.makedirs('dirname1/dirname2')
> 可生成多层递归目录

* os.mkdir('dirname')
> 生成单级目录


## 删除目录
* os.removedirs('dirname1')
> 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推

* os.rmdir('dirname')
> 删除单级目录，若目录不为空则无法删除

## 删除文件
* os.remove()
> 删除一个文件


## 重命名
* os.rename("oldname","newname")
> 重命名目录/文件

## 获取信息
* os.stat('path/filename')
> 获取文件/目录信息

## 判断文件还是目录
* os.path.isfile(path)
> 如果path是一个文件，则返回True

* os.path.isdir(path)
> 如果path是一个目录，则返回True

## 改变文件路径
* os.chdir("dirname")
> 改变当前脚本工作目录；相当于shell下cd

## 分割文件名与目录
* os.path.split()
> 返回一个文件名和目录名

## 分离文件名和扩展名
* os.path.splitext()

## 规范path字符串形式
* os.path.normpath(path)

---



# 其他方法
* os.system("bash command")
> 运行shell命令，直接显示

* os.popen("bash command).read()
> 运行shell命令，获取执行结果

* os.exit()
> 终止当前进程

* os.environ
> 获取系统环境变量


---

# os.stat()结构
```
st_mode: inode 保护模式
st_ino: inode 节点号
st_dev: inode 驻留的设备
st_nlink: inode 的链接数
st_uid: 所有者的用户ID
st_gid: 所有者的组ID
st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据
st_atime: 上次访问的时间
st_mtime: 最后一次修改的时间
st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）
```

---

# 转载
http://www.cnblogs.com/Eva-J/articles/7228075.html#_label5