#dannie  2018/9/26  15:47  PyCharm
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
import pandas as pd

asender='dannie.lei@jaspercapital.com'#发件人
areceiver='dannie.lei@jasperam.com,dannie.lei@jaspercapital.com'#收件人
acc='dannie.lei@jaspercapital.com,dannie.lei@jasperam.com'#抄送人
ausername='dannie.lei@jaspercapital.com'#账号
apassword='******'#密码
title= '邮件主题'#邮件主题
text = '邮件正文'#邮件正文
html_text = """
<p>邮件正文</p>
""" #html正文
filenames=[r'C:\Users\jasper\Desktop\新建文件夹\text.xlsx',r'C:\Users\jasper\Desktop\新建文件夹\text2.txt']#附件地址,注意文件名为英文
picture=r'C:\Users\jasper\Desktop\新建文件夹\1.png'#加载图片地址
df=pd.DataFrame([['one', '1'], ['two', '2']], columns=['name', 'value'])#表格

msg = MIMEMultipart()
msg['Subject'] = title
msg['From'] = asender
msg['To'] = areceiver
msg['Cc'] = acc

# 文本
# text_plain = MIMEText(text,'plain', 'utf-8')
# msg.attach(text_plain)

#html文本
# text_html = MIMEText(html_text,'html', 'utf-8')
# msg.attach(text_html)

#表格
html=df.to_html()
# df_html = MIMEText(html,'html', 'utf-8')
# msg.attach(df_html)

# 图片
body = """
    <img src="cid:image1"/>
    """
msg.attach(MIMEText(html_text+body+html, 'html', 'utf-8')) # html_text+body+html：html文本+加载图片+表格
with open(picture, 'rb') as f:
    msgImage = MIMEImage(f.read())
msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

# 附件
for filename in filenames:
    with open(filename, 'rb') as f:
        mime = MIMEBase('application', 'octet-stream')
        mime.add_header('Content-Disposition', 'attachment', filename=filename.split('\\')[-1])
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)

smtp = smtplib.SMTP()
smtp.connect('c1.icoremail.net')
smtp.login(ausername,apassword)
smtp.sendmail(asender, areceiver.split(',') + acc.split(','), msg.as_string())
smtp.quit()
