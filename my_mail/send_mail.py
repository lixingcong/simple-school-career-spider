#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年8月28日

@author: li
'''
import my_mail_accounts

from smtplib import SMTP_SSL
from email.MIMEText import MIMEText
from email.mime.multipart import MIMEMultipart
def send_email(email_content):
	try:
		msg = MIMEMultipart('alternative')
		msg['Content-Type'] = "text/html; charset=utf-8"
		msg['Subject'] = my_mail_accounts.subject
		msg['From'] = my_mail_accounts.sender
		msg['To'] = ','.join(my_mail_accounts.destination)

		# 指定_charser为utf-8否则中文无法在某些邮件客户端正确显示
		HTML_BODY = MIMEText(email_content.encode('utf-8'), 'html', _charset = 'utf-8')
		msg.attach(HTML_BODY)
		conn = SMTP_SSL(my_mail_accounts.SMTPserver, 465)
		conn.set_debuglevel(False)
		conn.login(my_mail_accounts.USERNAME, my_mail_accounts.PASSWORD)

		try:
			conn.sendmail(my_mail_accounts.sender, my_mail_accounts.destination, msg.as_string())
		finally:
			conn.close()
	except Exception, exc:
		print exc
		
if __name__ == '__main__':
	with open("/tmp/1.html",'rb') as f:
		send_email(f.read().decode('utf-8'))
