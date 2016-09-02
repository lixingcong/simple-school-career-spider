#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月2日
@author: li
'''
from mail_accounts.mail_account_example import MAIL_ACCOUNT_EXAMPLE


if __name__ == '__main__':
	# Attention: assume that you had file '/tmp/GuangZhou_spider.html'' exsits!
	my_mail = MAIL_ACCOUNT_EXAMPLE()  # __init__() method is linking to file '/tmp/GuangZhou_spider.html'
	my_mail.send_mail()
