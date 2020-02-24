# @Author：只因不值得
import exrex,os
from optparse import OptionParser
from colorama import init,Fore

def save():
    savefile = open("../save.txt", "w+")
    return savefile

# 生成密码字典
def make_pwd():
    savefile = save()

    if options.mod == "0":
        print(Fore.GREEN + "[+] 正在生成, 请稍后" + Fore.WHITE)
        for pwd in pwdict:
            if options.file == "pwd.txt":
                pwd100s = open(options.file, "r")
            else:
                if os.path.exists(options.file):
                    pwd100s = open(options.file, "r")
                else:
                    print(Fore.RED+"\n[-] 没有该文件, 正在退出"+Fore.WHITE)
                    exit(0)
            for top100 in pwd100s:
                savefile.write(pwd +top100.strip("\n")+"\n")
                savefile.write(pwd.capitalize() + top100.strip("\n") + "\n")
                savefile.write(top100.strip("\n") + pwd + "\n")
                savefile.write(top100.strip("\n") + pwd.capitalize() + "\n")
        print(Fore.GREEN + "[+] 开始去重! " + Fore.WHITE)
        clean_100()
        print(Fore.GREEN + "[+] 去重完成! " + Fore.WHITE)
        savefile.close()
    elif options.mod == "1":
        print(Fore.GREEN + "[+] 正在生成, 请稍后" + Fore.WHITE)
        for pwd1 in pwdict:
            for pwd2 in pwdict:
                savefile.write(pwd1 + pwd2 + "\n")
                savefile.write(pwd2 + pwd1 + "\n")
                two_payload = list(exrex.generate("{0}(|!|@|#|$|%|){1}".format(pwd1, pwd2)))
                one_payload = list(exrex.generate("{0}(|!|@|#|$|%|)".format(pwd1)))
                for i in two_payload:
                    savefile.write(i + "\n")
                for j in one_payload:
                    savefile.write(j + "\n")
        print(Fore.GREEN + "[+] 开始去重! " + Fore.WHITE)
        clean_pwd()
        print(Fore.GREEN + "[+] 去重完成! " + Fore.WHITE)
        savefile.close()
    else:
        print(Fore.RED+"\n[-] 模式错误, 正在退出"+Fore.WHITE)
        exit(0)

    print(Fore.GREEN + "[+] 生成完成! " + Fore.WHITE)

# 自定义字典去重
def clean_pwd():
    clean_files = open("../save.txt", "r")
    [pwd.add(i.strip("\n")) for i in clean_files]
    save_file = save()
    if options.case == "0":
        [save_file.write(j+"\n") for j in pwd if len(j) > 4]
    elif options.case == "1":
        [save_file.write(j.lower() + "\n") for j in pwd if len(j) > 4]
    elif options.case == "2":
        [save_file.write(j.upper() + "\n") for j in pwd if len(j) > 4]
    elif options.case == "3":
        [save_file.write(j.capitalize() + "\n") for j in pwd if len(j) > 4]
    else:
        print(Fore.RED+"\n[-] 大小写模式错误, 正在退出"+Fore.WHITE)
        exit(0)
    save_file.close()

# top100拼接字典去重
def clean_100():
    clean_files = open("../save.txt", "r")
    [pwd.add(i.strip("\n")) for i in clean_files]
    save_file = save()
    [save_file.write(j + "\n") for j in pwd if len(j) > 4]
    save_file.close()

if __name__ == "__main__":
    pwd = set()
    pwdict = []
    init(wrap=True)
    parse = OptionParser("%prog [options] arg .... , 如果多个请用 | 分隔 如: -n 'pwd | name'")
    parse.add_option("-n",help="姓名",dest="name",default=None)
    parse.add_option("-j", help="姓名简写",dest="minname",default=None)
    parse.add_option("-q",help="QQ号",dest="QQ",default=None)
    parse.add_option("-i",help="手机号",dest="ipone",default=None)
    parse.add_option("-d",help="出生年月",dest="day",default=None)
    parse.add_option("-e",help="邮箱",dest="email",default=None)
    parse.add_option("-b",help="伴侣",dest="girlfriend",default=None)
    parse.add_option("-p",help = "历史密码",dest="hpwd",default=None)
    parse.add_option("-c", help="大小写, 全部小写: 1， 全部大写: 2, 开头大写: 3, 默认为0不开启,仅限混乱模式", dest="case", default="0")
    parse.add_option("-m", help="模式，top100模式: 0 (默认), 混乱模式: 1", dest="mod", default="0")
    parse.add_option("-f", help="自定义TOP100文件,默认组合字典: pwd.txt", dest="file", default="pwd.txt")
    (options, args) = parse.parse_args()

    if options.name and options.name != "":
        for i in options.name.split("|"):
            pwdict.append(i.strip(" "))

    if options.minname and options.minname != "":
        for i in options.minname.split("|"):
            pwdict.append(i.strip(" "))

    if options.QQ and options.QQ != "":
        for i in options.QQ.split("|"):
            pwdict.append(i.strip(" "))

    if options.ipone and options.ipone != "":
        for i in options.ipone.split("|"):
            pwdict.append(i.strip(" "))

    if options.day and options.day != "":
        for i in options.day.split("|"):
            pwdict.append(i.strip(" "))

    if options.email and options.email != "":
        for i in options.email.split("|"):
            pwdict.append(i.strip(" "))

    if options.girlfriend and options.girlfriend != "":
        for i in options.girlfriend.split("|"):
            pwdict.append(i.strip(" "))

    if options.hpwd and options.hpwd != "":
        for i in options.hpwd.split("|"):
            pwdict.append(i.strip(" "))

    make_pwd()