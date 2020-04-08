# @Author：只因不值得

import requests
from bs4 import BeautifulSoup

def get_html(url):
    header = {
        "Host": "my.vmware.com",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "Sec-Fetch-Dest": "document",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    req = requests.get(url,headers=header)
    if req.status_code == 200:
        html = req.text
        return html
    else:
        print("[-] 访问网站失败")
        exit(0)

def get_download_url(Version):
    url_1 = "https://my.vmware.com/cn/web/vmware/info/slug/desktop_end_user_computing/vmware_workstation_pro/15_0"
    html = BeautifulSoup(get_html(url_1),"lxml")
    if Version == 0:
        text = html.find_all("a",class_="button secondary")[0].get('href')
    else:
        text = html.find_all("a", class_="button secondary")[1].get('href')
    html2 = BeautifulSoup(get_html("https://my.vmware.com/"+text),'lxml')
    text2 = html2.find_all("span",class_="fileNameHolder")[0].string
    download_url = "http://download3.vmware.com/software/wkst/file/"+text2
    print("\n下载链接: "+download_url)


if __name__ == "__main__":
    print("""
    Vmware官方下载链接获取
    """)
    print("> Windiws最新版: 0（默认）")
    print("> Linux最新版: 1\n")
    Version = input("请输入系统 > ")
    if Version == "":
        Version = 0
    get_download_url(Version)






