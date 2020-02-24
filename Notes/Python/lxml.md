# 简介

`Xpath`：一种XML路径语言，通过该语言可以在XML文档中迅速的查找到相应的信息，Xpath表达式叫做Xpath selector



---



# 选取节点

* `nodename`：选取此节点的所有子节点

* `/`：使用`/`可以选择某个标签，并且可以使用`/`进行多层标签的查找

  ```
  # 选取根元素下的body节点
  
  /body
  ```

* `//`：可以提取某个标签的所有信息

  ```
  //book
  ```

* `@`：选取某个节点的属性

  ```
  # 获取某class属性下的某个标签内容
  
  //标签[@class="属性"]
  ```







# 谓语

用来查找某个特定的几点或者某个指定的值的节点，被嵌在方括号中 `[]`



例子

* 选取bookstore下的第一个子元素

  ```
  /bookstore/book[1]
  ```

* 选取bookstore下的倒数第二个book元素

  ```
  /bookstore/book[last()]
  ```

* 选取bookstore下前面两个子元素

  ```
  /bookstore/book[position() < 3]
  ```

* 选取拥有price属性的book元素

  ```
  //book/[@price]
  ```

* 选取所有属性price等于10的book元素

  ```
  //book[@price=10]
  ```



---



# 通配符

* `*`：匹配任意节点
* `@*`：匹配节点中的任何属性



---



# 选取多个路径

通过在路径表达式中使用 `|` 运算符，可以选择若干个路径

```
//bookstore/book | //book/title

# 选取所有book元素，以及book元素下所有的title元素
```



---



# 运算符

| 运算符 | 描述 | 例子 |
| :----: | :------------: | :------------------------: |
| \| | 计算两个节点集 | //book \| //cd |
| + | 加法 | 6+4 |
| - | 减法 | 6-4 |
| * | 乘法 | 6*4 |
| div | 除法 | 8 div 4 |
| = | 等于 | price = 9.8 |
| != | 不等于 | price != 9.8 |
| < | 小于 | price < 9.8 |
| < = | 小于或等于 | price <= 9.8 |
| > | 大于 | price > 9.8 |
| >= | 大于或等于 | price>=9.8 |
| or | 或 | price = 9.8 or price < 9.9 |
| and | 与 | price > 9 and price <10 |
| mod | 计算除法的余数 | 5 mod 2 |



---



# 方法

* 提取文本信息：`text()`
* 选取第几个节点：`position()=number`
* 选取最后一个节点：`last()`



---



# 例子

* 获取所有a标签的href属性值

  ```
  html.xpath("//a/@href")
  ```

* 获取attr对应的值

  ```
  //@attr
  ```

* attr属性值开头为strh的节点

  ```
  starts-with(@attr,strh)
  ```

* atrr属性值是否包含substr

  ```
  contains(@attr,substr)
  ```

  



---



# lxml库

`lxml`库是一个HTML/XML的解析库，主要是解析和提取HTML/XML数据

python 3.x之后 lxml库便没有自带的`etree`，解决方法

```
pip install lxml==3.7.2
```



导入模块

```python
from lxml import etree
```



*基本使用*：

* `html = etree.HTML("string")`：将字符串解析为HTML文档

* `etree.tostring(html,encoding='utf-8',pretty_print=True).decode('utf-8')`：按字符串序列化为HTML文档

* `etree.parse()`：读取文件

  ```python
  from lxml.html import etree
  html = etree.parse('files/hello.html')
  result = etree.tostring(html, encoding='utf-8', pretty_print=True).decode('utf-8')
  print(result)
  ```

  > Ps：使用`etree.parse()`方法解析html内容时，会报`lxml.etree.XMLSyntaxError`错误
  >
  > 因为`etree.parse()`默认使用xml的解析器，当html内容不规范或标签没闭合时，就会报错
  >
  > 解决方法：使用`etree.HTMLParser()`作为`etree.parse()`方法的参数即可

* `etree.HTMLParser()`：创建一个HTML的解析器

  ```python
  htmlParser = etree.HTMLParser(encoding='utf-8')
  html = etree.parse('files/hello.html', parser=htmlParser)
  result = etree.tostring(html, encoding='utf-8', pretty_print=True).decode('utf-8')
  print(result)
  ```

* 在lxml中使用XPATH语法：`.xpath('xpath语法')`，返回的是一个列表

  ```python
  from lxml.html import etree
  htmlParser = etree.HTMLParser(encoding='utf-8')
  html = etree.parse('files/hello.html', parser=htmlParser)
  # htmlText = etree.tostring(html, encoding='utf-8', pretty_print=True).decode('utf-8')
  # print(htmlText)
  lis = html.xpath('//li')
  for li in lis:
      print(etree.tostring(li, encoding='utf-8', pretty_print=True).decode('utf-8'), end='')
  aList = html.xpath('//a/@href')
  for a in aList:
      print(a)
  print('-----------------------')
  lis = html.xpath('//li')
  for li in lis:
      # . 号表示在当前的 li 元素下去匹配
      href = li.xpath('.//a/@href')[0] #获取 a 标签的 href 属性
      txt = li.xpath('.//a/text()')[0] #获取 a 标签的文本
      print(href, txt)
  ```
