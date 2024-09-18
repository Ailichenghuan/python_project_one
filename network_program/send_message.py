import urllib.parse
import http.client
import json


def main():
    host  = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    # 下面的参数需要填入自己注册的账号和对应的密码
    params = urllib.parse.urlencode({'account': '你自己的账号', 'password' : '你自己的密码', 'content': '您的验证码是：147258。请不要把验证码泄露给其他人。', 'mobile': '接收者的手机号', 'format':'json' })
    # 将一个字典类型的参数转换成url格式的参数，常用于构建get请求的参数。
    print(params)
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)    # 创建了一个HTTP连接
    conn.request('POST', sms_send_uri, params, headers) # params 接收一个字典或者字符串的查询参数
    # 组合成一个完整url地址
    response = conn.getresponse()
    response_str = response.read()  # 返回的是响应内容的字节串
    jsonstr = response_str.decode('utf-8')
    print(json.loads(jsonstr))
    conn.close()


if __name__ == '__main__':
    main()