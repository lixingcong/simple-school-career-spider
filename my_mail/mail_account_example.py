#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2016年8月29日

@author: li
'''
from my_mail.mail_account_base import MAIL_ACCOUNT_BASE

class MAIL_ACCOUNT_EXAMPLE(MAIL_ACCOUNT_BASE):
	def __init__(self):
		MAIL_ACCOUNT_BASE.__init__(self, 'sender@qq.com', 'password', 'smtp.qq.com', ['tom@qq.com','Jane@qq.com'], '近期宣讲会', '/tmp/GuangZhou_spider.html', True)

if __name__ == '__main__':
	my_mail_account=MAIL_ACCOUNT_EXAMPLE()
	# send it!
	my_mail_account.send_mail()
	
