# coding:utf-8
import yagmail
from UI import run_1
# 连接邮箱服务器
def send_mail(ave):
    yag = yagmail.SMTP(
        user="wyj1215127@163.com",  # 邮箱账号
        password="FKXAYTDXBEYPWUAV",  # 邮箱开通smtp服务授权码
        host="smtp.163.com",  # 服务器地址
        smtp_ssl = True #如果用的是qq邮箱或者你们公司的邮箱使用安全协议的话，必须写上smtp_ssl = True
    )
    # 发送邮件
    yag.send(
        to=['downey.wang@chang-e.cn'],  # 如果是多个收件人的话，写成list就行了
        # cc='417418104@qq.com',  # 抄送
        subject='CB Test测试报告',  # 邮件标题
        # contents='测试报告',  # 邮件正文
        attachments=[r'C:\Users\bob\PycharmProjects\pythonProject1\UI\report\\'+ave]
    )
    yag.close()
    print("已发送测试报告到邮件")

