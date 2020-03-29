常量
====
在pywifi中定义了以下`constatns`
在使用常量之前，请记住`import pywifi`

连接wifi配置信息
===========
一个配置文件是我们要连接到AP的设置
```python
from pywifi import const #导入wifi模块的定义
```

<!--more-->

创建wifi连接配置
---------------
`pywifi.Profile()`  #创建wifi连接文件

配置文件的字段:
`.ssid` - AP的ssid
`.auth` - AP的认证算法
`.akm` - AP的密钥管理类型
`.cipher` - AP的密码类型
`.key(optinoal)` - AP的关键。如果密码不是这个，应该设置它`CIPHER_TYPE_NONE`

```python
profile = pywifi.Profile() #创建wifi配置文件
profile.ssid = "***" #wifi名称
profile.auth = const.AUTH_ALG_OPEN #网卡开放
profile.akm.append(const.AKM_TYPE_WPA2PSK) #设置wifi的加密类型
profile.cipher = const.CIPHER_TYPE_CCMP #加载单元
profile.key = '*****' #wifi密码
```


认证算法
--------
认证算法应该被分配非一个配置文件
对于正常情况,几乎所有的AP都使用开放算法
```
const.AUTH_OPEN
const.AUTH_SHARED
```


wifi加密类型
-----------
密钥管理类型应分配给配置文件
对于普通的接入点

根据对应wifi的加密模式吧akm设置为相应的加密方式
AP没有安全设置，`AKM_TYPE_NONE`
AP处于WPA模式， `AKM_TYUPE_WPAPSK`
AP处于WPA2模式， `AKM_TYUPE_WPA2PSK`

`AKM_TYPE_WPA`并`AKM_TYPE_WPA2`通过企业的AP使用
```
const.AKM_TYPE_NONE
const.AKM_TYPE_WPA
const.AKM_TYPE_WPAPSK
const.AKM_TYPE_WPA2
const.AKM_TYPE_WPA2PSK
```


加密单元
--------
如果akm不是，则应将密码类型设置为配置文件`AKM_TYPE_NONE`
您可以参考您想要连接的AP的设置
```
const.CIPHER_TYPE_NONE
const.CIPHER_TYPE_WEP
const.CIPHER_TYPE_TKIP
const.CIPHER_TYPE_CCMP
```


连接wifi的对象(接口)
============
一个接口意味着我们用它来执行Wi-Fi运营的Wi-Fi接口(例如，扫描，连接，断开，...)

获取网卡信息
------------
一般来说,平台只会有一个WIFI接口,因此,使用索引 0 来获取WIFI接口
```python
import pywifi

wifi = pywifi.PyWiFi() #抓取网卡接口

iface = wifi.interfaces()[0] #获取网卡

```


输出无线网卡名称
-----------------
`interface.name()`

```python
wifi = pywifi.PyWiFi() #抓取网卡接口

#可能你有很多无线网卡,你可以根据对应的下标获取相应的网卡
#来进行对wifi的破解
iface = wifi.interfaces()[0] #获取网卡
print(iface.name())
```


扫描wifi 和 获取扫描结果
-----------------
`interface.scan()` 扫描wifi
`interface.scan_results()` 获取扫描结果,一个配置文件`列表`将被返回

`.bssid` mac地址

注意:因为每个WiFi接口的扫描时间都是不同的
```python
import pywifi
wifi = pywifi.PyWiFi() #抓取网卡接口
iface = wifi.interfaces()[0] #获取网卡
print(iface.name())

iface.scan() #对wifi进行扫描
time.sleep(5)

bassess = iface.scan_results() #扫描结果

for i in bessis:
    if(i.ssid != ''):
        print('[+] '+i.bssid+'===>'+i.ssid+'\n') 
```


添加 和 删除 wifi配置信息
------------------------
`interface.add_network_profile(profiles)` 添加wifi配置信息

`interface.remove_all_network_profiles()` 删除wifi配置信息

---


通过返回一个配置文件列表获取所有保存的AP配置文件
--------------------------------------------
`interface.network_profiles()`


连接到指定的wifi 和 断开wifi连接
-------------------------------
注意: `.add_network_profile(profiles)`应该使用在`connect(profile)`调用之前

`interface.connect(profile)` 连接到指定wifi

`interface.disconnect()` 断开wifi连接

```python
import pywifi
from pywifi import const

profile = pywifi.Profile()
profile.ssid = "只因不值得"
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = '*******'

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
iface.add_network_profile(profile)
iface.connect(profile) #连接到指定wifi

if iface.status() in [const.IFACE_CONNECTING,const.IFACE_CONNECTED]:
    iface.disconnect()
    #通过判断wifi为连接和连通状态 来断开wifi连接
```



获取当前网卡状态 和 网卡状态有哪些
==================================
`interface.status()` 获取当前的网卡状态

网卡状态有以下几种
```python
#断开
const.IFACE_DISCONNECTED

#扫描
const.IFACE_SCANNING

#无效
const.IFACE_INACTIVE

#连接
const.IFACE_CONNECTING

#接通
const.IFACE_CONNECTED
```

通过判断现在网卡返回的状态码
来显示现在网卡的状态
```python
import pywifi
from pywifi import const

wifi = pywifi.PyWiFi() #获取网卡接口
iface = wifi.interfaces()[0] #获取网卡

#判断网卡现在的状态
if iface.status() in [const.IFACE_INACTIVE,const.IFACE_DISCONNECTED]:
    print("连接失败")
else:
    print("连接成功")
```

```


例如
```python
import pywifi

profile = pywifi.Profile()
profile.ssid = 'testap'
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = '12345678'

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
profile = iface.add_network_profile(profile)
iface.connect(profile)
```