from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def main():
    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    sever = socket(family=AF_INET, type=SOCK_STREAM)    # 服务器端先初始化Socket，然后与端口绑定(bind)，对端口进行监听(listen)，调用accept阻塞，等待客户端连接。
    # 2.绑定IP地址和端口(端口用于区分不同的服务)
    # 同一时间在同一个端口上只能绑定一个服务否则报错
    sever.bind(('192.168.137.1', 6789))
    # 3.开启监听 - 监听客户端连接到服务器
    # 参数512可以理解为连接队列的大小
    sever.listen(512)
    print('服务器启动开始监听...')
    while True:
       # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
        client, addr = sever.accept()
        print(str(addr) + '连接到了服务器')
        # 5.发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6.断开链接
        client.close()

# telnet 192.168.137.1 6789
# telnet就是查看某个端口是否可访问。

# 客户端初始化一个Socket，然后连接服务器(connect)，
# 如果连接成功，这时客户端与服务器端的连接就建立了。客户端发送数据请求，
# 服务器端接收请求并处理请求，然后把回应数据发送给客户端，客户端读取数据，最后关闭连接，一次交互结束。