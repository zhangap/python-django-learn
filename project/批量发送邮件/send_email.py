# 发送邮件
# 读取excel模块 pip install xlrd
import os
import time

import pandas as pd
import ssl

# 发邮件的包
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送者邮箱
sender_email = '1130139617@qq.com'
# 发送者
sender_name = '武当三丰'
# 邮箱密码
sender_pass = 'lydpaalvxszxbacg'
# 邮件服务器
server = None


def send_mail(to_person, titleTxt, content):
    # 主题
    title = Header(titleTxt, 'utf-8')

    # 发送内容
    msg = MIMEText(content, 'html', 'utf-8')
    msg['From'] = f'"{Header(sender_name, "utf-8").encode()}" <{sender_email}>'
    msg['To'] = to_person
    msg['Subject'] = title
    # 发送邮件
    global server
    server.sendmail(sender_email, to_person, msg.as_string())


def login_email_server():
    # 创建安全链接
    context = ssl.create_default_context()
    # 连接服务器
    global server
    server = smtplib.SMTP('smtp.qq.com')
    # 识别客户端
    server.ehlo()
    # 加密连接
    server.starttls(context=context)
    # 重新识别
    server.ehlo()
    # 登录邮箱
    server.login(sender_email, sender_pass)


def init():
    # 拿到当前执行文件的路径
    current_path = os.path.dirname(os.path.abspath(__file__))
    print(current_path)
    data = pd.read_excel(os.path.join(current_path, '员工名单.xlsx'))

    # 循环查找
    for index, row in data.iterrows():
        # 注意：就算是批量发送邮件，这里也需要重新登录邮件服务器
        login_email_server()
        # print(row['姓名'])
        # 构造邮件内容
        content = f'亲爱的{row["name"]}同学,感谢您对公司的付出,您的工资由以前的<span style="color:red;">{row["original"]}</span>调整为现在的<span style="color:green;font-weight:bold;">{row["now"]}</span>'
        print(content, row['email'])
        to_email = row['email']
        if to_email:
            send_mail(to_email, '工资调整通知', content)
            time.sleep(1)


if __name__ == '__main__':
    init()
    # login_email_server()
    # send_mail('1069478502@qq.com', '测试', '<h1>这个是测试邮件</h1>')
