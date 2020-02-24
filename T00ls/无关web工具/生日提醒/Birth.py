# @Author：只因不值得

import zhdate
import config
import datetime


def Get_Birthday():
    days = 0
    todays = datetime.datetime.now().strftime("%Y-%m-%d").split("-")

    while 10 != days:
        dt_date2 = zhdate.datetime(int(todays[0]), int(todays[1]), int(todays[2]) + days)
        nl_todays = zhdate.ZhDate.from_datetime(dt_date2)  # 公历转农历
        nl_toda = str(nl_todays).strip("农历").replace('年', '-').replace('月', '-').replace('日', '')  # 数字农历

        # 取月日
        numbers = nl_toda.split("-")
        nl_today = numbers[1] + numbers[2]

        for i in config.birth:
            birthdays = config.birth[i].split("-")
            try:
                birthday = birthdays[1] + birthdays[2]
            except:
                birthday = birthdays[0] + birthdays[1]

            if nl_today == birthday:
                dt_date1 = nl_todays.to_datetime() # 农历转公历日期
                Birth_day = "{0}：{1}".format(i,str(dt_date1).split(" ")[0])
                email(Birth_day)
                print(Birth_day)
        days = days + 1


def email(Birth_day):
    import smtplib
    from email.mime.text import MIMEText

    message = MIMEText(Birth_day, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "温馨提示"
    message['To'] = ",".join(config.receivers)
    message['Subject'] = "生日提示"

    try:
        s = smtplib.SMTP_SSL(config.email_host, 465)
        s.login(config.email_user, config.email_pass) # 登陆邮箱
        s.sendmail(config.sender, [config.receivers,], message.as_string()) # 发送邮件！
        print('Done.sent email success')
    except smtplib.SMTPException:
        print('Error.sent email fail')

if __name__ == "__main__":
    Get_Birthday()
