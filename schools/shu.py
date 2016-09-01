#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月1日
@author: li
'''
from schools.school_base import SCHOOL_BASE
import requests
from bs4 import BeautifulSoup

class SCHOOL_SHU(SCHOOL_BASE):
	def __init__(self, isFromLocal=False):
		SCHOOL_BASE.__init__(self, u'上海大学', u'http://zbb.shu.edu.cn', u'http://zbb.shu.edu.cn/PositionList.aspx', isFromLocal=isFromLocal)
		self.header['X-MicrosoftAjax'] = 'Delta = true'
		self.header['X-Requested-With'] = 'XMLHttpRequest'
		self.payload = {
			'__VIEWSTATEGENERATOR':'',
			'__VIEWSTATE': '',
			'__EVENTVALIDATION': '',
			'ctl00$content$ddlXL':u'本科',
			'ctl00$content$ddlJobNature':u'全职',
			'ctl00$content$ddlReleaseDate':'7',
			'ctl00$content$btnSearch':u'职位搜索'
		}
		
	def open_url_and_get_page(self):
		if self.isFromLocal is False:
			conn = requests.get(self.url, headers=self.header)
			res = BeautifulSoup(conn.content, "html.parser")
			ev = res.select("#__EVENTVALIDATION")[0]["value"]
			vs = res.select("#__VIEWSTATE")[0]["value"]
			vsg = res.select("#__VIEWSTATEGENERATOR")[0]["value"]
			self.payload["__EVENTVALIDATION"] = ev
			self.payload["__VIEWSTATEGENERATOR"] = vsg
			self.payload["__VIEWSTATE"] = vs
			conn = requests.post(self.url, headers=self.header, timeout=60, data=self.payload)
			self.content_original = conn.content
			
		else:
			with open('/tmp/req.html', 'rb') as f:
				self.content_original = f.read().decode('utf-8')
		pass		
	
	def get_HTML(self):
		return self.content_original
	
if __name__ == '__main__':
	obj=SCHOOL_SHU(True)
	obj.open_url_and_get_page()	
	print obj.get_HTML()
