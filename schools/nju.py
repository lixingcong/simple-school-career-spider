#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月1日
@author: li
'''
from bs4 import BeautifulSoup
import requests
from schools.school_base import SCHOOL_BASE

class SCHOOL_NJU(SCHOOL_BASE):
	def get_HTML(self):
		return self.content_original
		
if __name__ == '__main__':
	obj=SCHOOL_NJU(u'南京大学',u'http://job.nju.edu.cn:9081',u'/login/nju/home.jsp?type=zph&pageNow=1&sfss=sfss&zphzt=&jbksrq=&jbjsrq=2016-09-20&sfgq=&pageSearch=1',isFromLocal=True)
	obj.open_url_and_get_page()
	print obj.get_HTML()
	
	