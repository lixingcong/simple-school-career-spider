#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月2日
@author: li
'''
from smtplib import SMTP_SSL
from email.MIMEText import MIMEText
from email.mime.multipart import MIMEMultipart

class MAIL_ACCOUNT_BASE(object):
	def __init__(self, sender, password, smtp_server, destination=None, subject=None, content=None, isFromLocalHTMLFile=False):
		self.sender = sender
		self.password = password
		self.smtp_server = smtp_server
		self.destination = destination
		self.subject = subject
		
		if isFromLocalHTMLFile is False:  # content is plain text HTML
			self.content = content
		else:  # content is link to a file
			with open(content, 'rb') as f:
				self.content = f.read().decode('utf-8')
		
	def send_mail(self, destination=None, subject=None, content=None):
		if destination is None:
			destination = self.destination
		if subject is None:
			subject = self.subject
		if content is None:
			content = self.content
		try:
			msg = MIMEMultipart('alternative')
			msg['Content-Type'] = "text/html; charset=utf-8"
			msg['Subject'] = subject
			msg['From'] = self.sender
			msg['To'] = ','.join(destination)
	
			# 指定_charser为utf-8否则中文无法在某些邮件客户端正确显示
			HTML_BODY = MIMEText(content.encode('utf-8'), 'html', _charset='utf-8')
			msg.attach(HTML_BODY)
			
			conn = SMTP_SSL(self.smtp_server, 465)
			conn.set_debuglevel(False)
			conn.login(self.sender, self.password)
	
			try:
				conn.sendmail(self.sender, destination, msg.as_string())
			finally:
				conn.close()
				
		except Exception, exc:
			print exc
		
		
