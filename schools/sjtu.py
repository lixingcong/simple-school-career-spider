#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月1日
@author: li
'''
import re
import requests
from schools.school_base import SCHOOL_BASE


class SCHOOL_SJTU(SCHOOL_BASE): 
	def __init__(self, title, host, url, encode=None, isFromLocal=False):
		SCHOOL_BASE.__init__(self, title, host, url, encode=encode, isFromLocal=isFromLocal)
		
	
	
	def find_parameters_and_get_real_link(self,input_string):
		# input string should be like this:
		# <a class="sy_a" href="javascript:void(0);" onclick="viewDwzpxx('PPaDGP38YQTscYHmhM3pWt', 'jygl_scfwyrdw')">康龙公司</a>
		partern = re.compile("viewDwzpxx\(.*\)\">")
		result = partern.findall(input_string)
		if result:
			result = result[0].split('\'')
			for i in result:
				print i
		else:
			print "no found"

if __name__ == '__main__':
	obj=SCHOOL_SJTU(u'上海交通大学',u'http://www.job.sjtu.edu.cn',u'/eweb/jygl/zpfw.so?modcode=jygl_zpxxck&subsyscode=zpfw&type=searchZpxx&zpxxType=new',isFromLocal=True)
	