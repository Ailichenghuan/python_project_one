from time import time
from threading import Thread

import requests

# 继承Thread类创建自定义的线程类
class Download_Handler(Thread):
    def __init__(self, url):
        super().__init__()
        self_url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/User/Hao/' + filename, 'wb') as f:
            f.write(resp.content)

def main():
    # 通过requests模块的get函数获取网络资源
    resp = requests.get('https://apis.tianapi.com/topnews/index?key=276d4391c55b8b74a52d79525bb77f99')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['result']['list']:
        url = mm_dict['picUrl']
        # 通过多线程方式实现图片下载
        Download_Handler(url).start()

if __name__ == '__main__':
    main()