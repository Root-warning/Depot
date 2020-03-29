## 0x00 简介
通过Python操作注册表主要有两种方式
1.通过Python的内置模块`_winreg`
2.Win32 Extension for Python的`win32api模块`

windows注册表的组成是由`类似键值对`组成的
`key`键
`Value`值分三种:`name`,`type`,`data`

<!--more-->

## 创建和修改注册表

### 读取 `.OpenKey()` 和 `.OpenKeyEx()`
`_winreg.Openkey(key,sub_key,res=0,sam=KEY_READ)`
打开指定的键，返回一个句柄对象
参数说明:
    `key`是一个已经打开的键，或者是任何一个预定义的 `HKEY_*常量`
    `sub_key`是标识要打开的子键的字符串
    `res`是一个保留整数，并且必须为零,默认值为零
    `sam`是一个整数,用于指定描述所需密钥安全访问的访问掩码。默认是`KEY_READ`
结果是指定键的新句柄

`如果该功能失败,windowsError则引发`

`_winreg.OpenKeyEx()`
通过`OpenKey()`使用默认参数来提供功能

### 创建Key `CreateKey()`
`_winreg.CreateKey(key,sub_key[,res[,sam]])`
创建或打开指定得到键,返回一个 句柄对象
参数说明:
    `key`是一个已经打开的键，或者是任何一个预定义的 `HKEY_*常量`
    `sub_key`是一个字符串，用于命名此方法打开或创建的密钥。
    如果key是预定义键之一，则sub_key可能是`None`。在这种情况下，返回的句柄是传递给该函数的相同的键句柄。
    如果密钥已经存在，该功能将打开现有密钥。
    返回值是打开的键的句柄。如果该功能失败， `WindowsError`则会引发异常。

### 删除Key `DeleteKey`
`_winreg.DeleteKey(key,sub_key)`
删除指定的密钥
此方法不能使用子密钥删除密钥
如果方法成功，则删除整个键（包括其所有值）
如果该方法失败，WindowsError则会引发异常

### 删除键值 `DeleteValue`
` _winreg.DeleteValue(key,value)`
从注册表项中删除一个命名值。
参数说明:
    `key`是一个已经打开的键，或者是一个预定义的 HKEY_ *常量
    `value`是标识要删除的值的字符串。

### 给新建的key赋值 `.SetValue`
`_winreg.SetValue(key,sub_key,type,value)`
将值与指定的键关联
参数说明:
    `key`是一个已经打开的键，或者是一个预定义的 HKEY_ *常量。
    `sub_key`是一个字符串，用于命名与其关联的子键。
    `type`是一个指定数据类型的整数。目前这个必须是`REG_SZ`，意味着只支持字符串。使用`SetValueEx()`功能支持其他数据类型
    `value`是一个指定新值的字符串
如果由sub_key参数指定的键不存在，则SetValue函数会创建它。
值的长度受可用内存的限制。长值（超过2048字节）应该以文件形式存储在配置注册表中。这有助于注册表高效地执行。
由关键参数标识的关键字必须已打开才能 KEY_SET_VALUE访问

## 使用例子
使用例子1
```python
#!/usr/bin/env python
#coding=utf-8
import _winreg

key=_winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer")

#删除键
_winreg.DeleteKey(key, "Advanced")

#删除键值
_winreg.DeleteValue(key, "IconUnderline")

#创建新的
newKey = _winreg.CreateKey(key,"MyNewkey")

#给新创建的键添加键值
_winreg.SetValue(newKey,"ValueName",0,"ValueContent")
```

使用例子2
```python
import _winreg
handler=_winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,'SOFTWARE\Classes')
key= _winreg.EnumKey(handler,1)
key=_winreg.OpenKey(handler,str(key))
val= _winreg.EnumValue(key,1)
print val
```

## 其他函数和作用
`CloseKey()` – 关闭一个Key
`ConnectRegistry()` – 链接到其他机器的注册表
`EnumKey()` – 为已经打开的Key里面的子键建立索引
`EnumValue()` – 为打开的键中的值建立索引
`FlushKey()` – 回写所有的键属性改变到注册表
`LoadKey()` – 从指定文件读入键信息
`QueryValue()` – 在注册表中检索一个键的路径
`QueryValueEx()` – 注册表中检索一个键的路径
`QueryInfoKey()` – 返回关于键的信息
`SaveKey()` – 保存键到文件
`SetValue()` – 设置一个键
`SetValueEx()` – 设置一个值

## 参考链接
官网: https://docs.python.org/2/library/_winreg.html
其他链接:http://blog.sina.com.cn/s/blog_1574497330102wjfg.html

非原创，纯属学习笔记