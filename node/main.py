# 获取网路上的信息，网络空间测绘引擎
import requests


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something Wrong！"
    

if __name__ == "__main__":
    url = "http://www.baidu.com"
    print(get_html(url)[:1000])
