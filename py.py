#dannie  2018/9/26  15:47  PyCharm
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

asender='dannie.lei@jaspercapital.com'#发件人
areceiver='dannie.lei@jasperam.com,1242405137@qq.com'#收件人
acc='1242405137@qq.com,dannie.lei@jasperam.com'#抄送人
ausername='dannie.lei@jaspercapital.com'#账号
apassword='706148'#密码
title= '邮件主题'#邮件主题
text = '邮件正文'#邮件正文
filenames=[r'C:\Users\jasper\Desktop\新建文件夹\text.xlsx',r'C:\Users\jasper\Desktop\新建文件夹\text2.txt']#附件地址,注意文件名为英文

def __init__(self):
    msg = MIMEMultipart('mixed')
msg['Subject'] = title
msg['From'] = asender
msg['To'] = areceiver
msg['Cc'] = acc
class mailsender(object):
    #正文
    def message(self,text):
        text_plain = MIMEText(text,'plain', 'utf-8')
        msg.attach(text_plain)

#附件
    def add_attachment(self, filenames):
        for filename in filenames:
            with open(filename, 'rb') as f:
                mime = MIMEBase('application', 'octet-stream')
                mime.add_header('Content-Disposition', 'attachment', filename=filename.split('\\')[-1])
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                mime.set_payload(f.read())
                encoders.encode_base64(mime)
                msg.attach(mime)

def login(self,ausername,apassword)
    smtp = smtplib.SMTP_SSL()
    smtp.connect('c1.icoremail.net')
    smtp.login(ausername,apassword)
    smtp.sendmail(asender, areceiver.split(',') + acc.split(','), msg.as_string())
    smtp.quit()
