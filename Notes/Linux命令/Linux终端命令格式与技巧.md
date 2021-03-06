## 声明
转载自黑马视频中的笔记！

---

## 终端命令格式
```
command [-options] [parameter]
```

说明：

* `command`：命令名
* `-options`：选项，可用来对命令进行控制，也可以省略
* `parameter`：传送命令的参数，可以是零个，一个或者多个
* `[ ]`：代表可选


<!--more-->

---

## 查阅命令帮助信息

### --help
```
command --help
```
说明：
* 显示`command `命令的帮助信息


### man
```
man command 
```
说明
* 查阅`command `命令的使用手册
> `man`是manual的缩写，是Linux提供的一个手册，包含了绝大部分的命令，函数的详细使用说明


使用`man`时的操作键

|操作键|功能|
|:--:|:--:|
|空格键|显示手册页的下一屏|
|Ent 键|一次滚动手册页的一行|
|b|回滚一屏|
|f|前滚一屏|
|q|退出|
|/word|搜索word字符串|


---


## 小技巧
`ctrl+shift+=` 加大终端字体
`ctrl+-` 缩小终端字体

---


## 自动补全
在敲出`文件/目录/命令`的前几个字母之后，按下`tab`键
* 如果输入的没有歧义，系统会自动补全
* 如果还存在其他`文件/目录/命令`，再按一下`tab`键，系统会提示可能存在的命令


---


## 曾经使用过的命令
按 `上/下`光标键可以在曾经使用过的命令之间来回切换
如果想要退出选择，并且不想执行当前选择的命令，可以按`ctrl+c`


---


## 当前目录和上级目录
`.`代表当前目录
`..`代表上一级别目录

---


