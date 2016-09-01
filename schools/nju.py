#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月1日
@author: li
'''
from bs4 import BeautifulSoup
import requests
from schools.school_base import SCHOOL_BASE
import time

class SCHOOL_NJU(SCHOOL_BASE):
	def __init__(self, title, host, url, encode=None, isFromLocal=False):
		SCHOOL_BASE.__init__(self, title, host, url, encode=encode, isFromLocal=isFromLocal)
		self.begin_date=''
		self.end_date=''
		
	def open_url_and_get_page(self):
		# open page and it should be decoded here
		if self.isFromLocal is False:
			self.calc_delta_date()
			url=u'/login/nju/home.jsp?type=zph&pageNow=1&sfss=sfss&zphzt=&jbksrq='+self.begin_date+u'&jbjsrq='+self.end_date+u'&sfgq=&pageSearch=1'
			conn = requests.get(self.host + url, headers=self.header)
			self.content_original = conn.content
		else:
			with open('/tmp/req.html', 'rb') as f:
				self.content_original = f.read().decode('utf-8')
		pass
	
	def get_HTML(self):
		return self.content_original
	
	def calc_delta_date(self):
		from datetime import datetime,timedelta  		
		now = datetime.now()  
		now_delta_10days = now + timedelta(days=10)
		yesterday = now - timedelta(days=1)
		self.end_date=now_delta_10days.strftime("%Y-%m-%d")
		self.begin_date=yesterday.strftime("%Y-%m-%d")

		
if __name__ == '__main__':
	obj=SCHOOL_NJU(u'南京大学',u'http://job.nju.edu.cn:9081',u'',isFromLocal=False)
	obj.open_url_and_get_page()
	print obj.get_HTML()
	
	