# _*_coding:utf-8_*_
"""
# @Author  : Guangqiang Li
# @Time    : 2021/7/12 9:42
# @Description:
"""
import re
import requests
import time
import random
import os


def get_blog_url(url, pages=1):
    '''
    获取包含所有博文url的列表
    url地址是个人主页（一般第一页会省略/article/list/1为了格式统一加上去)
    pages是博文列表的页数（默认一页）
    '''
    pattern = r"(https://blog.csdn.net/weixin_42409884/article/details/[\d]+)"
    blog_url = []
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'}
    for i in range(1, pages+1):
        try:
            response = requests.get(url+"{}".format(i), headers=headers)
        except:
            print("OOps, we can't get your blog list")
            os._exit(0)
        blog_url += re.findall(pattern, response.text)
        # blog_url = re.findall(pattern, response.text)
    print('博客地址', blog_url)
    # blog_url = ['https://blog.csdn.net/weixin_42409884/article/details/109293327']
    return blog_url

# 获取包含所有博文url的列表
all_blog_url = get_blog_url(url="https://blog.csdn.net/weixin_42409884/article/list/", pages=2)
print("You have {} blogs".format(len(all_blog_url)))


def get_user_agent(url):
    # 获取包含若干user_agent的列表
    pattern = r'<tbody><tr><td>(.*?)</td>'
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'}
    try:
        response = requests.get(url=url, headers=headers)
    except:
        print("OOps, we can't get user agent list, you should fix it manully")
        os._exit(0)
    user_agent = re.findall(pattern, response.text)
    return user_agent

# 获取包含若干user_agent的列表
all_user_agent = get_user_agent("https://deviceatlas.com/blog/list-of-user-agent-strings#android")
print("You have got {} user agent".format(len(all_user_agent)))

'''
从这几个网址找的代理
http://free-proxy.cz/en/proxylist/country/all/http/ping/level1
http://nntime.com/proxy-list-01.htm
https://hidemy.name/en/proxy-list/?maxtime=500&type=h&start=256#list
'''
http_pro=['134.209.29.120:3128','161.35.70.249:8080','176.9.75.42:8080','88.198.50.103:8080','88.198.24.108:3128','176.9.119.170:3128','88.198.24.108:8080','134.209.29.120:8080','176.9.75.42:3128','46.4.96.137:3128','46.4.96.137:8080','173.212.202.65:80','87.241.88.44:18617','172.67.181.112:80','88.198.50.103:3128','176.9.119.170:8080','172.67.181.28:80','172.67.182.150:80','172.67.181.84:80','172.67.182.142:80','172.67.181.1:80','172.67.182.59:80','172.67.181.82:80','172.67.181.92:80','172.67.182.102:80','172.67.181.62:80','172.67.222.111:80','172.67.182.115:80','172.67.182.72:80','172.67.181.70:80','172.67.182.109:80','165.22.81.30:43630','178.208.226.230:49538','172.67.181.166:80','172.67.181.152:80','167.71.5.83:8080','141.101.114.26:80','142.93.130.126:80','172.67.181.173:80','172.67.181.165:80','172.67.182.152:80','172.67.182.136:80','172.67.181.181:80','172.67.182.147:80','172.67.181.54:80','172.67.181.11:80','172.67.181.10:80','172.67.181.14:80','172.67.181.21:80','172.67.181.32:80','172.67.182.163:80','172.67.182.158:80','172.67.181.143:80','172.67.181.58:80','172.67.182.38:80','172.67.182.105:80','172.67.181.162:80','172.67.182.17:80','172.67.181.123:80','172.67.182.121:80','172.67.128.116:80','172.67.181.52:80','172.67.182.116:80','172.67.181.49:80','172.67.182.27:80','172.67.181.140:80','95.141.193.14:80','172.67.182.78:80','172.67.181.138:80','172.67.182.83:80','172.67.181.129:80','172.67.181.91:80','172.67.182.140:80','172.67.182.118:80','172.67.182.161:80','172.67.182.100:80','172.67.181.30:80','172.67.182.165:80','172.67.181.5:80','172.67.181.130:80','172.67.182.16:80','172.67.181.97:80','172.67.182.113:80','172.67.181.168:80','172.67.182.62:80','172.67.182.107:80','172.67.182.69:80','172.67.182.25:80','172.67.182.103:80','172.67.181.77:80','172.67.182.64:80','172.67.182.153:80','172.67.181.149:80','172.67.181.69:80','172.67.181.98:80','172.67.182.6:80','172.67.182.77:80','172.67.181.147:80','172.67.182.0:80','172.67.181.72:80','172.67.182.79:80','95.141.193.35:80','172.67.181.176:80','172.67.181.74:80','172.67.181.36:80','172.67.182.34:80','172.67.181.85:80','172.67.182.90:80','172.67.181.3:80','172.67.182.125:80','172.67.182.2:80','172.67.181.145:80','172.67.182.5:80','172.67.182.35:80','172.67.146.139:80','172.67.181.122:80','172.67.182.131:80','172.67.182.155:80','172.67.181.101:80','190.93.245.26:80','172.67.182.127:80','172.67.182.23:80','190.93.247.58:80','172.67.181.174:80','172.67.181.16:80','172.67.181.171:80','172.67.181.126:80','172.67.181.113:80','172.67.181.116:80','172.67.181.158:80','172.67.181.110:80','190.93.247.25:80','172.67.181.164:80','172.67.181.142:80','172.67.181.170:80','172.67.181.17:80','172.67.181.180:80','172.67.181.9:80','172.67.181.87:80','18.185.60.249:80','172.67.182.55:80','172.67.181.115:80','172.67.182.39:80','172.67.182.119:80','172.67.181.61:80','172.67.182.130:80','172.67.182.52:80','172.67.181.128:80','141.101.115.26:80','172.67.182.10:80','172.67.182.68:80','172.67.182.97:80','172.67.181.76:80','172.67.181.144:80','172.67.182.58:80','172.67.182.149:80','172.67.181.44:80','172.67.181.94:80','172.67.182.139:80','172.67.181.12:80','172.67.181.4:80','172.67.139.99:80','172.67.182.124:80','172.67.182.128:80','172.67.182.48:80','172.67.181.41:80','172.67.182.174:80','172.67.181.135:80','172.67.182.32:80','172.67.182.8:80','172.67.181.23:80','172.67.181.155:80','172.67.181.156:80','172.67.181.136:80','172.67.182.31:80','172.67.182.132:80','141.101.121.217:80','172.67.182.53:80','172.67.182.145:80','172.67.182.40:80','172.67.182.19:80','172.67.181.35:80','172.67.182.93:80','172.67.181.93:80','172.67.181.120:80','172.67.181.40:80','172.67.182.1:80','172.67.181.25:80','172.67.181.106:80','172.67.182.137:80','172.67.182.94:80','172.67.182.71:80','172.67.182.126:80','172.67.182.88:80','172.67.182.141:80','172.67.182.45:80','172.67.182.29:80','172.67.181.167:80','172.67.182.3:80','172.67.181.37:80','172.67.182.41:80','172.67.181.68:80','172.67.181.42:80','172.67.182.96:80','172.67.181.108:80','172.67.182.56:80','172.67.181.18:80','172.67.181.154:80','172.67.181.45:80','172.67.181.51:80','172.67.182.162:80','172.67.182.138:80','172.67.181.89:80','172.67.181.124:80','46.4.96.137:8080','188.165.141.114:3129','78.37.94.172:8080','172.67.182.47:80','172.67.182.134:80','172.67.182.14:80','172.67.182.99:80','172.67.182.92:80','190.93.247.2:80','172.67.182.143:80','172.67.182.98:80','172.67.181.2:80','172.67.182.84:80','172.67.181.20:80','172.67.182.144:80','172.67.181.160:80','172.67.182.76:80','172.67.182.114:80','172.67.182.63:80','172.67.182.22:80','172.67.181.19:80','172.67.181.79:80','172.67.181.6:80','172.67.182.117:80','172.67.181.26:80','172.67.181.118:80','172.67.181.7:80','172.67.182.157:80','172.67.182.146:80','172.67.181.47:80','172.67.182.9:80','172.67.182.4:80','190.93.244.26:80','172.67.181.150:80','172.67.182.169:80','51.38.81.148:8080','172.67.181.100:80','172.67.182.37:80','172.67.181.103:80','172.67.182.49:80','172.67.182.120:80','172.67.181.107:80','172.67.181.34:80','172.67.182.85:80','172.67.182.11:80','172.67.181.60:80','172.67.181.63:80','172.67.181.65:80','172.67.182.104:80','172.67.181.111:80','172.67.181.55:80','141.101.114.87:80','172.67.182.36:80','172.67.182.51:80','172.67.182.28:80','172.67.181.75:80','172.67.181.121:80','172.67.182.164:80','141.101.123.21:80','172.67.182.67:80','172.67.182.60:80','81.5.103.14:8081','172.67.181.33:80','134.122.120.49:8118','54.152.162.43:80','52.251.79.6:3128','52.251.79.1:3128','52.251.79.13:3128','169.57.1.85:8123','104.211.29.96:80','20.50.215.47:3128','20.51.89.234:3128','169.57.1.84:25','83.96.237.121:80','116.203.155.45:8118','51.254.98.24:80','95.217.179.118:8080','80.48.119.28:8080','161.202.226.194:80','195.154.237.156:3838','94.30.97.245:80','169.57.157.148:25','104.248.48.186:31583','104.248.63.18:31583','157.230.103.189:44253','169.57.157.146:8123','119.81.189.194:80','34.64.222.158:80','104.248.48.239:31583','119.81.71.27:80','20.46.192.88:3128','20.46.192.87:3128','15.206.242.126:80','165.22.81.30:42087','51.178.49.77:3131','117.51.157.6:8118','139.129.99.186:8080','128.199.200.108:8118']
print("You have got {} proxies host".format(len(http_pro)))

import telnetlib
# 连接Telnet服务器，随机选一个上文的代理服务器测试一下是否可用
[ip, port] = random.choice(http_pro).split(sep=":")
try:
    tn = telnetlib.Telnet(ip,port=port,timeout=20)
except:
    print('You proxy host is bad')
else:
    print('You proxy host is good')


i = 0
while True:
    proxies = {'http': '{}'.format(random.choice(http_pro))}
    # url = random.choice(all_blog_url) # 随机挑选一个访问
    url = all_blog_url[i%len(all_blog_url)] # 按照顺序依次访问
    headers = {
        'Referer': 'https://blog.csdn.net',
        'User-Agent': random.choice(all_user_agent)
        }

    i += 1
    try:
        requests.get(url, headers=headers, proxies=proxies)
    except:
        print("something wrong")
        os._exit(0)
    time.sleep(random.random()/1000)
    if i%(len(all_blog_url)*1)==0:
        print("this is the {}th time".format(int(i/len(all_blog_url)))) # 每整体循环一次输出一下