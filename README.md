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
