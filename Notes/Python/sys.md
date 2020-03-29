# 简介
sys模块是与python解释器交互的一个接口

<!--more-->

---

# 常用方法

* sys.argv
> 实现从程序外部向程序内部传递参数
```python
ret = sys.argv
username = ret[0]
password = ret[1]
或
username = sys.argv[0]
password = sys.argv[1]
```

* sys.exit([arg])
> 程序中间的退出
> 0为正常退出
> 1为异常退出

* sys.getdefaultencoding()
> 获取系统当前编码

* sys.setdefaultencoding()
> 设置系统默认编码
> 执行dir（sys）时不会看到这个方法，在解释器中执行不通过，可以先执行reload(sys)
> 在执行 setdefaultencoding('utf8')，此时将系统默认编码设置为utf8。（见设置系统默认编码 ）

* sys.getfilesystemencoding()
> 获取文件系统使用编码方式，Windows下返回'mbcs'，mac下返回'utf-8'

* sys.path
> 获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到

* sys.platform
> 操作系统平台名称

* sys.version
> 获取Python解释器的版本