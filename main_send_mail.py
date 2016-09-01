#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月2日
@author: li
'''
from my_mail.send_mail import send_email

if __name__ == '__main__':
	with open('/tmp/GuangZhou_spider.html','rb') as f: 
		send_email(f.read().decode('utf-8'))