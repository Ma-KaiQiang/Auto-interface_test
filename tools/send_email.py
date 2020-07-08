# coding:utf8
'''
@Time    : 2020/7/7 9:30
@Author  : MaKaiQiang
@File    : unit_management_case.py
'''
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sent_info = {'sender': '1121624020@qq.com',
             'receviers': ['mkq@gato.com.cn'],
             'authorization_code': 'myokicbspdzsgjjc',
             'subject': '接口自动化测试项目'
             }


class SentEmail():

    def __init__(self,text=None):
        # 创建一个带附件的实例
        text='''
        各位好!

            附件为此次自动化测试运行结果，请收阅。

        '''
        self.message = MIMEMultipart()
        self.message['From'] = Header("云平台自动化接口测试", 'utf-8')
        self.message['To'] = Header("云平台项目组", 'utf-8')
        self.message['Subject'] = Header(sent_info['subject'], 'utf-8')
        # 邮件正文内容
        self.message.attach(MIMEText(text, 'plain', 'utf-8'))
        # 构造附件1，传送当前目录下的 report 文件
        with open(r'E:\Auto-interface\report\test_report.html', 'rb') as fp:
            att1 = MIMEText(fp.read(), 'base64', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="AutoTestReport.html"'
        self.message.attach(att1)

    # # 构造附件2，传送当前目录下的 runoob.txt 文件
    # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
    # message.attach(att2)
    def sent_email(self):
        try:
            smtpObj = SMTP_SSL('smtp.qq.com')
            smtpObj.ehlo('smtp.qq.com')
            smtpObj.login(sent_info['sender'], sent_info['authorization_code'])
            smtpObj.sendmail(sent_info['sender'], sent_info['receviers'], self.message.as_string())
            print("邮件发送成功")
        except Exception as e:
            print("Error: 无法发送邮件")
            raise e


if __name__ == '__main__':
    s=SentEmail()
    s.sent_email()