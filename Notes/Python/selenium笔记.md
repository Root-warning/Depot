感谢各位作者，此笔记是搜集整合的！

# AJAX简介

`AJAX`：异步Javascript和XML，通过在后台与服务器进行少量数据交换

Ajax可以使网页异步更新，意味着可以在不重新加载整个网页的情况下，对网页的某个部分进行更新

* 传统的网页（不使用Ajax）

  > 更新内容，必须重新加载整个网页



使用Ajax加载的数据，即使使用了JS，将数据渲染到了浏览器

在页面源代码中还是不能看到通过ajax加载的数据，只能看到使用这个URL加载的html代码



---



# 获取Ajax数据

* 直接分析`ajax`调用的接口，然后通过代码请求这个接口
* 使用`Selenium + chromedrive`模拟浏览器行为获取数据



---



# Selenium

* 安装Selenium

  ```pytho
  pip install selenium
  ```

* 下载相应驱动完成后，放到不需要权限的纯英文目录下就可以了

  ```
  Chrome：https://sites.google.com/a/chromium.org/chromedriver/downloads
  Firefox：https://github.com/mozilla/geckodriver/releases
  Edge：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
  Safari：https://webkit.org/blog/6900/webdriver-support-in-safari-10/
  ```

  



```python
from selenium import webdriver

# chromedriver的绝对路径
driver_path = r"D:\ProgramApp\chromedriver\chromedriver.exe"

# 初始化一个Driver，并且指定chromedriver的路径
driver = webdriver.Chrome(executable_path=driver_path)

# 请求网页
driver.get("https://lncn.org")

# 获取网页源代码
print(driver.page_source)

```

---

## 浏览器设置

```python
from selenium import webdriver

# 浏览器对象设置
options = webdriver.ChromeOptions()
options.add_argument('--headless') # 无头模式
options.add_argument('--disable-gpu') # 避免一些浏览器bug
options.add_argument('disable-infobars')	# 隐藏正受自动化控制
options.add_argument('lang=zh_CN.UTF-8') # 中文

# 创建浏览器
driver_path = r"C:\Users\Sariel\AppData\Local\Programs\Python\Python37\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path,options=options)
```

> Ps：由于此处`chrome_options`有不明报错，所以此处调用options模式（无浏览器模式）
>
> 原写法：`driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)`



### 使用代理

```python
from selenium import webdriver

# 浏览器对象设置
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://110.77.1.244:8123') # 使用代理

# 创建浏览器
driver_path = r"C:\Users\Sariel\AppData\Local\Programs\Python\Python37\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path,options=options)
```

---

## 浏览器控制

* `driver.close()`：关闭当前页面
* `driver.quit()`：退出整个浏览器
* `driver.set_windows_size(x,y)`：浏览器窗口大小
* `driver.maximize_windows()`：浏览器全屏显示
* `driver.back()`：后退
* `driver.forward()`：前进
* `driver.refresh()`：刷新当前页面
* `driver.get_screenshot_as_file(filepath)`：窗口截图

## 定位元素

* `find_element_by_id`：根据ID来查找某个元素

  ```python
  submitTag = driver.find_element_by_id('su')
  submitTag1 = driver.find_element(By.ID,'su')
  ```

* `find_element_by_class_name`：根据类名查找元素

  ```python
  submitTag = driver.find_element_by_class_name('su')
  submitTag1 = driver.find_element(By.CLASS_NAME,'su')
  ```

* `find_element_by_name`：根据name属性的值来查找元素

  ```python
  submitTag = driver.find_element_by_name('su')
  submitTag1 = driver.find_element(By.NAME,'su')
  ```

* `find_element_by_tag_name`：根据标签名来查找元素

  ```python
  submitTag = driver.find_element_by_tag_name('su')
  submitTag1 = driver.find_element(By.TAG_NAME,'su')
  ```

* `find_element_by_xpath`：根据xpath语法来获取元素

  ```python
  submitTag = driver.find_element_by_xpath('//div')
  submitTag1 = driver.find_element(By.XPATH,'div')
  ```

* `find_element_by_css_selector`：根据css选择器选择元素

  ```python
  submitTag = driver.find_element_by_css_selector('//div')
  submitTag1 = driver.find_element(By.XPATH,'div')
  ```

* `find_element_by_link`：定位文本连接

  ```python
  <a class="mnav" name="tj_trnews" href="https://news.baidu.com">新闻</a>
  
  submitTag = driver.find_element_by_link('新闻')
  ```

* `find_element_by_partial_link_text`：对link的补充，获取文本连接较长的时候，取一部分定位

  ```python
  <a class="mnav" name="tj_trnews" href="https://news.baidu.com">一个很长很长的连接</a>
  
  submitTag = driver.find_element_by_partial_link_text('一个很长')
  ```

  

> Ps：
>
> `find_element` 是获取第一个满足条件的元素
>
> `find_elements`：获取所有满足条件的元素
>
> 如果选择的元素有多个并以空格隔开：（class = "top mg5"）
>
> class选择器`只要选取其中一个`即可，css选择器选取一个并在名称前加`.`：`.top`
>
> 当你使用的是By.xxx形式的时候，需要导入：By：`from selenium.webdriver.common.by import By`



---



## 操作元素

*流程*：

* 找到元素
* 操控它

### 常用方法

* `send_keys(value)`：输入文字
* `clear()`：清除内容
* `click()`：点击

### 例子

* 操作输入框

```python
inputTag = driver.find_element_by_id("kw")
inputTag.clear()
inputTag.send_keys('python')
```

* 选中`checkbook`标签

```python
rememberTag = driver.find_element_by_name("rememberMe")
rememberTag.click()
```

* 操作多选框（select）

  > Ps：select元素不能直接点击，因为点击后还需要选中元素

  select标签提供的类：`selenium.webdriver.support.ui.Select`

  将获取到的元素当成参数传入这个类中，创建这个对象，以后就可以使用这个对象进行选择了

  

```python
from selenium.webdriver.support.ui import Select

#选择标签，使用Select创建对象
selectTag = select(driver.find_element_by_name("jumpMenu"))

# 根据索引选择
selectTag.select_by_index(1)

# 根据值选择
selectTag.select_by_visible("www.95yueba.com")

# 根据可视的文本选择
selectTag.select_by_visible_text("68客户端")

# 取消选中的所有选项
selectTag.deselect_all()
```

## 鼠标事件

在`webDriver`中，将这些关于鼠标的操作方法封装到`ActionChains`类中



`ActionChains`中鼠标常用的方法：

* `perform()`：执行ActionChains中存储的行为
* `context_click()`：右及
* `double_click()`：双击
* `drag_and_drop`：拖动
* `move_to_element()`：鼠标悬停

> 更多方法：https://selenium-python.readthedocs.io/api.html



* 例子

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# chromedriver的绝对路径
driver_path = r"D:\ProgramApp\chromedriver\chromedriver.exe"

# 初始化一个Driver，并且指定chromedriver的路径
driver = webdriver.Chrome(executable_path=driver_path)

# 请求网页
driver.get("https://lncn.org")

# 定位元素
ssrs= driver.find_elements_by_class_name("mg5") # 获取按钮所在位置
action = ActionChains(driver)	# 创建对象
action.move_to_element(ssrs[0])	# 鼠标移动到按钮并暂停
ssr = action.click(ssrs[0]).perform() # 执行点击该按钮
```



---



## 键盘事件

`Keys()`类提供了键盘上几乎所有按键的方法

```python
from selenium.webdriver.common.keys import Keys
```



`send_keys()`方法可以用来模拟键盘输入，还可以用来输入键盘上的按键，甚至是组合键

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = r"C:\Users\Sariel\AppData\Local\Programs\Python\Python37\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("http://baidu.com")

# 输入框输入内容
driver.find_element_by_id('kw').send_keys("seleniumm")

# 删除多输入的一个m
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)

driver.quit()
```



*常用键盘*操作：

* `Keys.BACK_SPACE`：删除键
* `Keys.SPACE`：空格键
* `Keys.TAB`：制表键
* `Keys.ESCAPE`：回退键
* `Keys.ENTER`：回车键
* `Keys.CONTROL,'a'`：全选（Ctrl + A）
* `Keys.F1`：F1

.....依次类推

使用

```python
send_keys(Keys.CONTROL,'a')
```



---



## Cookie操作

* 获取所有cookie信息：`driver.get_cookies()`

  ```python
  for cookie in driver.get_cookies():
      print(cookie)
  ```

* 根据cookie的key获取value：`driver.get_cookie(key)`

  ```python
  value = driver.get_cookie(key)
  ```

* 删除所有的cookie：`driver.delete_all_cookies()`

* 删除某个cookie：`driver.delete_cookie(key,optionsString)`，key是要删除的cookie名称，optionsstring（cookie选项）

* 添加cookie：`driver.add_cookie(cookie_dict)`，字典对象必须有name和value值



---



## 多窗口和窗口切换

* `driver.execute_script('window.open(url)')`：利用Javascript语句打开新窗口

  ```python
  from selenium import webdriver
  
  driver_path = r"C:\Users\Sariel\AppData\Local\Programs\Python\Python37\chromedriver.exe"
  driver = webdriver.Chrome(executable_path=driver_path)
  driver.get("http://baidu.com")
  
  # 打开新窗口
  driver.execute_script("window.open('http://douban.com/')")
  ```

  > Ps：虽然打开了新的窗口，但是原窗口还是停留在原窗口，也就是百度窗口，需要切换窗口

* `driver.current_window_handle`：获取当前窗口的句柄
* `dirver.window_handles`：返回所有窗口的句柄到当前会话

* `switch_to.window()`：不同的窗口之间切换

  ```python
  driver_path = r"C:\Users\Sariel\AppData\Local\Programs\Python\Python37\chromedriver.exe"
  driver = webdriver.Chrome(executable_path=driver_path)
  driver.get("http://baidu.com")
  
  # 打开新窗口
  driver.execute_script("window.open('http://douban.com/')")
  
  # 返回所有窗口句柄
  print(driver.window_handles)
  
  # 切换窗口
  driver.switch_to.window(driver.window_handles[0])
  
  # 当前窗口url
  print(driver.current_url)
  
  driver.quit()
  ```

  

---



## 页面等待

Web应用程序使用Ajax技术，当浏览器在加载页面时，页面上的元素可能并不是同时被加载完成的



### 显式等待

显式等待：等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常（`TimeoutException`）等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常（`TimeoutException`）

使用`WebDriverWait`类，在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到，则抛出异常

并用`expected_conditions`类提供的方法，进行判断

* 导入

  ```python
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC
  ```

* `WebDriverWait()` 说明

  ```python
  WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
  '''
  参数说明：
  driver：浏览器驱动
  timeout：最长超时时间，默认0.5s
  poll_frequency：超时后的异常信息，默认为NoSuchElementException
  '''
  ```

  一般搭配`until()`或`until_not()`方法配合使用

  ```python
  # 调用该方法提供的驱动作为一个参数，直到返回值为True
  until(method,message='')
  
  # 调用该方法提供的驱动作为一个参数，直到返回值为Flase
  until_not(method,message='')
  ```

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver_path = r"C:\Users\Sariel\AppData\Local\Programs\Python\Python37\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("http://baidu.com")

# 等待5秒，查找不到该元素，则抛出异常
element = WebDriverWait(driver,timeout=5).until(EC.presence_of_all_elements_located((By.ID,"kw22")))
element.send_keys('selenium')
driver.quit()
```



其他expected_conditions提供的条件判断方法

| 方法                                   | 说明                                      |
| -------------------------------------- | ----------------------------------------- |
| title_is                               | 当前页面标题是否等于预期                  |
| title_contains                         | 当前页面的标题是否包含预期的字符串        |
| presence_of_ekement_located            | 元素是否被加载在DOM树里                   |
| visibility_of_element_located          | 元素是否可见（元素非隐藏，宽高不等于0）   |
| visibility_of                          | 接收的参数为定位后的元素                  |
| presence_of_all_element_located        | 是否至少有一个元素存在于DOM树中           |
| text_to_be_present_in_element          | 某个元素中的text是否包含了预期的字符串    |
| text_to_be_present_in_element_value    | 某个元素的value属性是否包含了预期的字符串 |
| frame_to_be_available_and_switch_to_it | 该表单是否可以切换进去                    |
| invisibility_of_element_located        | 某个元素是否存在于DOM树或不可见           |
| element_to_be_clickable                | 元素是否可见并且是可点击的                |
| staleness_of                           | 等到一个元素从DOM树中移除                 |
| element_to_be_selected                 | 某个元素是否被选中，一般用在下拉列表      |
| element_located_selection_state_to_be  | 与上个方法相同，接收的参数为定位          |
| alert_is_present                       | 判断页面上是否存在alert                   |



### 隐式等待

隐式等待：通过一定的时长等待页面上某元素加载完成，`driver.implicitly_wait(时长)`

> 如果超出了设置的时长还没被加载，则抛出`NoSuchElementException`异常

```python
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime

driver_path = r"C:\Users\Sariel\AppData\Local\Programs\Python\Python37\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

# 等待10秒
driver.implicitly_wait(10)
driver.get("http://baidu.com")

try:
    print(ctime())
    # 该元素查找不到，则抛出异常
    driver.find_element_by_id("kw22")
except NoSuchElementException as e:
    print(e)
finally:
    driver.quit()
```



---



## WebElement 接口常用方法

通常需要和页面交互的方法都由WebElement接口提供

* `submit()`：提交表单
* `get_attribute(name)`：获得元素属性值
* `screentshot`：获取当前页面的截图
* `size`：窗口大小
* `text`：获取元素的文本
* `is_displayed()`：是否用户可见

```python
driver.find_element_by_id("kw22").text
```


---

# 例子
通过QQ一键快捷登录并跳转到漏洞盒子

```python

# @Author：只因不值得

from selenium import webdriver
import time


def login():
    driver_path = r"C:\Users\Sariel\AppData\Local\Programs\Python\Python37\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get('https://account.tophant.com/login/') #进入登录界面
    driver.implicitly_wait(3)
    driver.find_element_by_xpath("//span[@class='way way-qq']").click()

    # 获取登录窗口ID
    login_windows = driver.current_window_handle

    # QQ一键登录
    for handle in driver.window_handles:
        if handle != login_windows:
            driver.switch_to.window(handle)
            driver.implicitly_wait(5)
            iframe = driver.find_element_by_xpath(".//*[@id='ptlogin_iframe']")
            driver.switch_to.frame(iframe)
            driver.find_element_by_xpath('//div[@class="qlogin"]/div[@class="qlogin_show"]/div[@class="qlogin_list"]/a/span[@class="img_out_focus"]').click()
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[0])

    # 选择漏洞盒子进行跳转
    dx_windows = driver.current_window_handle

    # 跳转到漏洞盒子
    driver.find_element_by_xpath('//*[@id="loginCenter"]/div/div/a[2]/span').click()
    for ld_window in driver.window_handles:
        if ld_window != dx_windows:
            driver.close()
            driver.switch_to.window(ld_window)
            driver.implicitly_wait(5)
            driver.find_element_by_xpath('//*[@id="two"]/ul/li[2]/a').click()

    return driver

def Bug():
    driver = login()
    driver.find_element_by_xpath('//*[@id="submitform"]/div[5]/div/div[1]/div').click()
    driver.find_element_by_xpath('//*[@id="submitform"]/div[5]/div/div[2]/div/ul/li[1]/a').click()
    driver.find_element_by_xpath('//*[@id="submitform"]/div[5]/div/div[2]/div/ul/ul[2]/li[2]/a').click()
    driver.find_element_by_xpath('//*[@id="submitform"]/div[11]/div/textarea').send_keys('测试一下')

    time.sleep(10)

if __name__ == "__main__":
    Bug()
```






