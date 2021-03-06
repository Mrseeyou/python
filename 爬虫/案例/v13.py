from urllib import request, parse
from http import cookiejar

# 创建cookiejar的案例
cookie = cookiejar.CookieJar()
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https请求管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def login():
    '''
    负责初次登陆
    需要输入用户名密码,用来获取cookie
    :return:
    '''

    # 此属性需要从源码登陆form的action属性中提取
    url = 'http://www.renren.com/PLogin.do'

    # 此属性需要从源码登陆form的两个对应input中提取
    data = {
        'email':'13112520315',
        'password':'249399289'
    }

    # 对数据进行编码解析
    data = parse.urlencode(data).encode()
    # 创建一个请求对象
    req = request.Request(url,data=data)

    # 使用opener发起请求
    rsq = opener.open(req)


def getHomePage():
    url = 'http://www.renren.com/973032462/newsfeed/photo'

    # 如果已经执行了login函数,则opener自动已经包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()

    with open("rsp3.html","w",encoding="utf-8") as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()
