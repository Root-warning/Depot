## socket
通常我们用一个socket表示"打开了一个网络链接"
而打开一个socket需要知道目标计算机的IP地址和端口号
再指定协议类型

套接字是一个双向的通信信道的端点
套接字可能在沟通过程,进程之间在同一台机器上,或在不同的计算机之间

要创建一个套接字必须使用socket模块的socket.socket()的方法


<!--more-->

## 创建socket对象
格式:`socket(family,type[,protocal])`

| family参数     | 描述                 |
| -------------  |:-------------:      |
| socket.AF_UNIX | unix本机之间进行通信 |
| socket.AF_INET | 使用IPv4            |
| socket.AF_INET6| 使用IPv6            |

| type参数           | 描述            |
| -----------------  |:-------------: |
| socket.SOCK_STREAM | TCP套接字类型   |
| socket.SOCK_DGRAM  | UDP套接字类型   |
| socket.SOCK_RAW    | 原始套接字类型,可以监听网卡上的所有数据帧            |
|socket.SOCK_SEQPACKET| 是一种可靠的UDP形式,即保证交付数据报但不保证顺序   |

```python
import socket

#创建TCP socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#创建UDP socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
```


## socket 函数

### 服务端socket函数
#### bind()
格式:`socket.bind(address)`
将套接字绑定到地址
在`AF_INET`下,以元组(host,port)的形式表示地址
>socket.bind(host,port)

#### listen()
格式:`socket.listen(backlog)`
启用服务器以接受链接
操作系统可以挂起的最大链接数量,至少为1
>socket.listen(5)

#### accept()
格式:`socket.accept()`
接收TCP连接并返回(conn,address)
conn 是socket对象,可以在连接上发送和接收数据
address 是链接客户端的地址
>conn,addr = s.accept()


### 客户端socket函数
#### connect()
格式:`socket.connect(address)`
要连接的IP与端口
连接到address处的套接字,一般address的格式为元组(host,port)
如果连接出错,返回soct.error错误
>s.connect((host,port))

#### connect_ex()
格式:`socket.connect_ex(address)`
功能与connect()相同
成功返回0,失败返回error的值


### 公共socket函数
#### recv()
格式:`socket.recv(bufsize[,flag])`
bufsize指定要接收的最大数据量
flag提供有关消息的其他信息,通常可以忽略
接收套接字的数据,数据以字符串形式返回
>s.recv(1024)

#### send()
格式:`socket.send(string[,flag])`
将数据发送到socket
返回值是要发送的字节数量
>s.send('xxxx')

#### sendall()
格式:`socket.sendall(string[,flag])`
完整发送TCP数据
但在返回之前会尝试发送所有数据
成功返回None,失败则抛出异常

#### close()
格式:`socket.close()`
关闭套接字
>s.close()

#### recvfrom()
格式:`socket.recvfrom(bufsize[.flag])`
接受UDP套接字的数据
但返回值是(data,address)
data是包含接收数据的字符串,address是发送数据的套接字地址。

#### sendto()
格式:`socket.sendto(string[,flag],address)`
发送UDP数据
address是形式为(ipaddr,port)的元组,指定远程地址
返回值是发送的字节数

#### getpeername()
格式:`socket.getpeername()`
返回连接套接字的远程地址
返回值通常是元组(ipaddr,port)

#### getsockname()
格式:`socket.getsockname()`
返回套接字自己的地址
返回值通常是元组(ipaddr,port)

#### setsockopt()
格式:`socket.setsockopt(level,optname,value)`
设置给定套接字选项的值

#### getsockopt()
格式:`socket.getsockopt(level,optname[.buflen])`
返回套接字选项的值

#### settimeout()
格式:`socket.settimeout(timeout)`
设置套接字操作的超时期
imeout是一个浮点数,单位是秒
值为None表示没有超时期
一般,超时期应该在刚创建套接字时设置,因为它们可能用于连接的操作(如connect())

#### gettimeout()
格式:`socket.gettimeout()`
返回当前超时期的值,单位是秒
如果没有设置超时期,则返回None

#### fileno()
格式:`socket.fileno()`
返回套接字的文件描述符

#### setblocking()
格式:`socket.setblocking(flag)`
如果flag为0,则将套接字设为非阻塞模式,否则将套接字设为阻塞模式（默认值）
非阻塞模式下,如果调用recv()没有发现任何数据,或send()调用无法立即发送数据
那么将引起socket.error异常

#### makefile()
格式:`socket.makefile()`
创建一个与该套接字相关连的文件

#### gethostbyname()
格式:`socket.gethostbyname(hostname)`
将主机名转换为IPV4格式,IPV4地址以字符串形式返回
例如:100.50.200.5
如果主机名称本身是IPv4地址,则它保持不变

#### gethostbyaddr()
格式：`socket.gethostbyaddr(ip_address)`
通过ip地址，返回包括主机名的三元组:(hostname,aliaslist,ipaddrlist)


## 乱写的tcp服务端,尚未改进
```python
#coding:utf-8

import socket

IP = '127.0.0.1'
port = 555

#创建socket链接
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定地址
s.bind((IP,port))
print "[*] %s:%s" % (IP,port)

#创建操作系统最大链接数
s.listen(2)

while True:
    #接受并返回数据
    conn,addr = s.accept()
    print "[*] Accepted connection: %s:%s" % (addr[0],addr[1])

    while True:
        #打印返回的数据
        request = conn.recv(1024)
        print "[+] Received: %s" % request

        #发送到客户端,表示接受成功
        conn.send('ok')

    #关闭链接
    conn.close()
```


## 乱写的tcp客户端
```python
#coding:utf-8

import socket

IP = '127.0.0.1'
port = 555

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((IP,port))

while True:
    cmd = raw_input("Please input cmd:")
    s.sendall(cmd)

    data = s.recv(1024)
    print data

s.close()
```


## 参考链接
https://www.cnblogs.com/wumingxiaoyao/p/7047658.html
https://docs.python.org/2/library/socket.html