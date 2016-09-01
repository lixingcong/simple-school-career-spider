#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月1日
@author: li
'''
from schools.school_base import SCHOOL_BASE
import requests
from bs4 import BeautifulSoup

class SCHOOL_SYSU(SCHOOL_BASE):
	def __init__(self, isFromLocal=False):
		SCHOOL_BASE.__init__(self, u'中山大学', u'http://career.sysu.edu.cn', u'/Management_Field/Public/LectureManage.aspx', isFromLocal=isFromLocal)
		self.payload = {
			'__VIEWSTATEGENERATOR':'',
			'__VIEWSTATE': '',
			'__EVENTVALIDATION': '',
			'__ASYNCPOST': 'true',
			'__EVENTTARGET': '',
			'__EVENTARGUMENT': ''
		}
		
	def open_url_and_get_page(self):
		if self.isFromLocal is False:
			conn = requests.get(self.host+self.url, headers=self.header, timeout=60)
			res = BeautifulSoup(conn.content, "html.parser")			

			self.payload["__EVENTVALIDATION"] = res.select("#__EVENTVALIDATION")[0]["value"]
			self.payload["__VIEWSTATEGENERATOR"] = res.select("#__VIEWSTATEGENERATOR")[0]["value"]
			self.payload["__VIEWSTATE"] = res.select("#__VIEWSTATE")[0]["value"]

			# update URL assigned by ASP.Net
			self.url = conn.url
			self.content_original = conn.content
		else:
			with open('/tmp/req.html', 'rb') as f:
				self.content_original = f.read().decode('utf-8')
		print self.content_original
	
if __name__ == '__main__':
	obj=SCHOOL_SYSU(False)
	obj.open_url_and_get_page()
