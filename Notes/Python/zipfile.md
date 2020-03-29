## 简介
zip日常使用是压缩跟解压操作
所以这个模块使用频率也是比较高

`zipfile`里有两个非常重要的class,分别是`ZipInfo`和`ZipFile`

ZipFile是主要的类，用来创建和读取zip文件
ZipInfo是存储的zip文件的每个文件的信息

<!--more-->


## 使用及其他方法

### 创建对象
`zipfile.ZipFile(filename[,mode[,compression[,allowZip64]]])`
参数说明
filename 文件对象
mode 可选 r w a 代表文件的打开方式
compression: 指出这个zipfile用什么压缩方法.
>默认是ZIP_STORED,另一种选择是ZIP_DEFLATED；

allowZip64：是个bool型变量.
>当设置为True的时候就是说可以用来创建大小大于2G的zip文件，默认值是True；
```python
import zipfile

zf = zipfile.ZipFile('2.zip','r')
```


### 关闭文件,结束时必须要有
`zipfile.close()`
在退出程序前必须关闭,否则不会写入重要记录。
```python
import zipfile
zf = zipfile.ZipFile('2.zip','r')
zf.close()
```


### 测试zip文件是否存在
`zipfile.is_zipfile("filename")`
测试filename的文件,看它是否是个有效的zipfile
真返回true，否则false
```python
zipfile.is_zipfile("2.zip")
```


### 读取压缩包文件信息
`zipfile.namelist()`
返回一个列表，内容是zip文件中所有子文件的path
```python
import zipfile
zf = zipfile.ZipFile('2.zip','r')
for name in zf.namelist():
    print name
# 1.php

print zf.namelist()
```

`zipfile.infolist()`
返回包含zipinfo每个归档成员的对象的列表
包含以下方法:`i.filename`,`.date_time`,`.file_size`
```python
import zipfile
zf = zipfile.ZipFile('2.zip','r')
for i in zf.infolist():
    print i.filename
    print i.date_time
    print i.file_size

# 1.php
# (2018, 3, 7, 12, 3, 20)
# 131
```

`zipfile.printdir()`
返回具体信息，包括每个文件的path,修改时间和大小
```python
import zipfile
zf = zipfile.ZipFile('1.zip','r')
print zf.printdir()
```


### 打开压缩包中的某个文件
`ZipFile.open(name[, mode[, password]])`
获取一个子文件的文件对象，可以将其用来read,readline,write等等操作
参数说明:
`name`名称或zipinfo对象
`mode`打开的模式，默认为'r'
`pwd`适用于加密文件的密码

注意:如果你选择的加密zip必须在后面pwd参数添加上正确密码，否则会报错
```python
import zipfile
zf = zipfile.ZipFile('2.zip','r')
print zf.open('1.php')
print zf.open('1.php').read()
```


### 解压数据
`zipfile.extractall([,path[,members[,pwd]]])`
将所有文件按照namelist中显示得那样的目录结构从当前zip中提取出来并放到path下
若目录不存在自动创建
参数说明:
`path`指定文件路径
`pwd`用于加密的密码，密码错误会报错


### 为zip设置默认密码
`zipfile.setpassword(pwd)`
将pwd设置为默认密码以提取加密文件


### 返回错误文件
`zipfile.testzip()`
读取zip中的所有文件，验证他们的CRC校验和。返回第一个损坏文件的名称，如果所有文件都是完整的就返回None
```python
a = zf.testzip()
```


### 写入文件
`zipfile.write(filename[,arcname[,compression_type]])`
参数说明:
`compression_type`指定了压缩格式
开方式一定要是w或者a才能顺利写入文件

默认打包，没有压缩数据，如果压缩，需要用zlib模块
```
zf = zipfile.ZipFile('zipfile_write.zip',mode='w')
try:
    print('adding readme.txt')
    zf.write('readme.txt')
finally:
    print('closing')
    zf.close()
```


参考链接:
官方文档:https://docs.python.org/2/library/zipfile.html
简书:https://docs.python.org/2/library/zipfile.html
brucewong0516的博客:http://blog.csdn.net/brucewong0516/article/details/79064384
