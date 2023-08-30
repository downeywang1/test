"""发送邮件"""
# import smtplib
# import os
# import logging
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
# from Conf.Config import smtp_cfg, email_cfg
#
# _FILESIZE = 20  # 单位M， 单个附件大小
# _FILECOUNT = 10  # 附件个数
# _smtp_cfg = smtp_cfg
# _email_cfg = email_cfg
# _logger = logging.getLogger('main.email')
#
#
# class Email:
#     def __init__(self, subject, context=None, attachment=None):
#         self.subject = subject
#         self.context = context
#         self.attachment = attachment
#         self.message = MIMEMultipart()
#         self._message_init()
#
#     def _message_init(self):
#         if self.subject:
#             self.message['subject'] = Header(self.subject, 'utf-8')  # 邮件标题
#         else:
#             raise ValueError("Invalid subject")
#
#         self.message['from'] = _email_cfg['sender']  # from
#         self.message['to'] = _email_cfg['receivers']  # to
#
#         if self.context:
#             self.message.attach(MIMEText(self.context, 'html', 'utf-8'))  # 邮件正文内容
#         # 邮件附件
#         if self.attachment:
#             if isinstance(self.attachment, str):
#                 self._attach(self.attachment)
#             if isinstance(self.attachment, list):
#                 count = 0
#                 for each in self.attachment:
#                     if count <= _FILECOUNT:
#                         self._attach(each)
#                         count += 1
#                     else:
#                         _logger.warning('Attachments is more than ', _FILECOUNT)
#                         break
#
#     def _attach(self, file):
#         if os.path.isfile(file) and os.path.getsize(file) <= _FILESIZE * 1024 * 1024:
#             attach = MIMEApplication(open(file, 'rb').read())
#             attach.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
#             attach["Content-Type"] = 'application/octet-stream'
#             self.message.attach(attach)
#         else:
#             _logger.error('The attachment is not exist or more than %sM: %s' % (_FILESIZE, file))
#
#     def send_mail(self):
#         s = smtplib.SMTP_SSL(_smtp_cfg['host'], int(_smtp_cfg['port']))
#         result = True
#         try:
#             s.login(self._smtp_cfg['user'], self._smtp_cfg['passwd'])
#             s.sendmail(self._smtp_cfg['sender'], self._smtp_cfg['receivers'], self.message.as_string())
#         except smtplib.SMTPException as e:
#             result = False
#             _logger.error('Send mail failed', exc_info=True)
#         finally:
#             s.close()
#         return result
#
#
# mail = Email(title, context, file)
# send = mail.send_mail()
# print(send)

# import smtplib
# import os
# import logging
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
# from Conf.Config import smtp_cfg, email_cfg
#
# _FILESIZE = 20  # 单位M， 单个附件大小
# _FILECOUNT = 10  # 附件个数
# _smtp_cfg = smtp_cfg
# _email_cfg = email_cfg
# _logger = logging.getLogger('main.email')
#
#
# class Email:
#     def __init__(self, subject, context=None, attachment=None):
#         self.subject = subject
#         self.context = context
#         self.attachment = attachment
#         self.message = MIMEMultipart()
#         self._message_init()
#
#     def _message_init(self):
#         if self.subject:
#             self.message['subject'] = Header(self.subject, 'utf-8')  # 邮件标题
#         else:
#             raise ValueError("Invalid subject")
#
#         self.message['from'] = _email_cfg['sender']  # from
#         self.message['to'] = _email_cfg['receivers']  # to
#
#         if self.context:
#             self.message.attach(MIMEText(self.context, 'html', 'utf-8'))  # 邮件正文内容
#         # 邮件附件
#         if self.attachment:
#             if isinstance(self.attachment, str):
#                 self._attach(self.attachment)
#             if isinstance(self.attachment, list):
#                 count = 0
#                 for each in self.attachment:
#                     if count <= _FILECOUNT:
#                         self._attach(each)
#                         count += 1
#                     else:
#                         _logger.warning('Attachments is more than ', _FILECOUNT)
#                         break
#
#     def _attach(self, file):
#         if os.path.isfile(file) and os.path.getsize(file) <= _FILESIZE * 1024 * 1024:
#             attach = MIMEApplication(open(file, 'rb').read())
#             attach.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
#             attach["Content-Type"] = 'application/octet-stream'
#             self.message.attach(attach)
#         else:
#             _logger.error('The attachment is not exist or more than %sM: %s' % (_FILESIZE, file))
#
#     def send_mail(self):
#         s = smtplib.SMTP_SSL(_smtp_cfg['host'], int(_smtp_cfg['port']))
#         result = False
#         try:
#             s.login(_smtp_cfg['user'], _smtp_cfg['passwd'])
#             s.sendmail(_email_cfg['sender'], _email_cfg['receivers'], self.message.as_string())
#             result = True
#         except smtplib.SMTPException as e:
#             result = False
#             _logger.error('Send mail failed', exc_info=True)
#         finally:
#             s.close()
#         return result
#

# # 示例调用代码
# title = "Test Email"
# context = "This is the email body."
# file = "/path/to/attachment.txt"
#
# mail = Email(title, context, file)
# send = mail.send_mail()
# print(send)
#
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
#
# def send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, attachment_path):
#     # 创建邮件对象
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = recipient_email
#     message["Subject"] = subject
#
#     # 添加邮件正文
#     message.attach(MIMEText(body, "plain"))
#
#     # 添加附件
#     with open(attachment_path, "rb") as attachment_file:
#         attachment = MIMEApplication(attachment_file.read())
#         attachment.add_header("Content-Disposition", "attachment", filename="C:/Users/Administrator/PycharmProjects/pythonProject/venv/report/DTC-230627095530.html")
#         message.attach(attachment)
#
#     # 连接到 Gmail SMTP 服务器
#     with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#         server.login(sender_email, sender_password)
#         server.send_message(message)
#
#
# # 设置发件人和收件人邮箱地址及授权信息
# sender_email = "mir.liu@dtcpay.com"
# sender_password = "qqyvpepbfajageqj"
# recipient_email = "mingmliu1@gmail.com"
#
# # 设置邮件主题、正文和附件路径
# subject = "Test Email with Attachment"
# body = "This is the email body."
# attachment_path = "C:/Users/Administrator/PycharmProjects/pythonProject/venv/report/DTC-230627095530.html"
#
# # 发送邮件
# send_email_with_attachment(sender_email, sender_password, recipient_email, subject, body, attachment_path)