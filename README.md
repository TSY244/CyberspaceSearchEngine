

# 免责声明

本工具仅供安全测试，严禁用于非法用途，后果与本团队无关

# 简介

本工具使用分布式的方式，对所指定的网络区域进行信息收集+漏洞爆破

# 环境配置

## elasticsearch

建议使用docker 搭建，这里放一个比较简单的搭建方式

https://blog.csdn.net/Acloasia/article/details/130683934

## redis

建议使用docker 搭建，这里放一个比较简单的搭建方式

https://blog.csdn.net/weixin_45821811/article/details/116211724

# 安装

## scan_server

考虑到需要对client 进行管理，所以直接使用python 运行就行了

### 直接运行

```
pip -r requirements.txt
python main
```



## scan_node

https://github.com/TSY244/scan_node

### docker

检查config.ini文件，修改必要的配置

```ini
[COMMON]
; 0: no conect to server, 1: conect to server
mode=1
server_ip=*
server_port=*
debug=0
use_log=1

[REDIS]
redis_host=*
redis_port=*
redis_password=*
message_queue=*

[IP_RANGE]
ip=192.168.79.0/24

[PORT_RANGE]
# for example: 1-65535 / 1-1000,2000-3000 / 1,2,3,4,5,6,7,8,9,10  /  1,2,3,1-100
port=1-10000

[elasticsearch]
host=*
port=*
; 不填默认info
info_index=
; 不填默认vuls
vuls_index=
; user=""
; passwd=""

[web_path_scanner]
; mode = dir or file
; if use file_path you can scan all file's web path
; if use file_name you can scan all web path in file
mode=dir
file_path=data/web_path/
file_name=dicc.txt
thread=30


[subdomain_scanner]
; mode = dir or file
; if use file_path you can scan all file's subdomain
; if use file_name you can scan all subdomain in file
mode=dir 
file_path=data/subdomain/
file_name=dict.txt
thread=20
```

请务必修改带`*` 部分的参数和看注释，尝试理解键名

使用

```
docker build .
```

### 直接运行

```python
pip -r requirements.txt
python main
```





# api

## info

path: /search/info?

example:http://127.0.0.1:8000/search/info?site=192.168.79.128&ports=1,2,3

| 参数  | 参数类型 | 描述                               | 例子                                                  |
| ----- | -------- | ---------------------------------- | ----------------------------------------------------- |
| site  | str      | 站点ip                             | http://127.0.0.1:8000/search/info?site=192.168.79.128 |
| porta | list     | 开放的端口，支持多个参数以逗号隔开 | http://127.0.0.1:8000/search/info?ports=1,2,3         |
| tide  | list     | 指纹                               | http://127.0.0.1:8000/search/info?tide=asdf           |
| area  | list     | 地区                               | http://127.0.0.1:8000/search/info?area=asdf           |
| tide  | list     | 指纹                               | http://127.0.0.1:8000/search/info?tide=java           |
| vuls  | list     | 漏洞                               | http://127.0.0.1:8000/search/info?vuls=ad             |

## vuls

http://127.0.0.1:8000/search/vuls?vul_type="任意文件上传漏洞"

| 参数     | 参数类型 | 描述     | 例子                                                         |
| -------- | -------- | -------- | ------------------------------------------------------------ |
| site     | str      | 站点ip   | http://127.0.0.1:8000/search/info?site=192.168.79.128        |
| vul_numb | string   | 漏洞编号 | http://127.0.0.1:8000/search/vuls?vul_numb=CVE-2018-3191     |
| prt_name | string   | 全名     | http://127.0.0.1:8000/search/vuls?prt_name="Oracle Weblogic: CVE-2018-2894" |
| vul_type | string   | 漏洞类型 | http://127.0.0.1:8000/search/vuls?vul_type="任意文件上传漏洞" |
