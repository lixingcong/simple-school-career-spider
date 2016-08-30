#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年8月30日
@author: li
'''
from schools.cumt import SCHOOL_CUMT
from schools.njust import SCHOOL_NJUST
from schools.njupt import SCHOOL_NJUPT

def add_serval_school_to_HTML_body(input_school_list):
	content = u'<html><head><meta charset="utf-8"><style>table, th, td { border: 1px solid #99cccc; text-align: left;}</style></head><body><h2>未来七日宣讲会</h2>'
	import time
	content += u'<p>发送时间：' + time.strftime("%Y-%m-%d %H:%M") + u'</p>'
	for i in input_school_list:
		content += i.get_HTML()
	content += u'<p>由<a href="http://lixingcong.github.io">Lixingcong</a>使用python强力驱动</p></body></html>' 
	return content
	
if __name__ == '__main__':
	result_list=[]
	# TODO: 多线程抓取，重写add_serval_school_toHTML函数
	cumt = SCHOOL_CUMT(u"中国矿业大学", u'http://jyzd.cumt.edu.cn', u'/teachin?time=60', isFromLocal=True)		
	result_list.append(cumt)
	
	njupt=SCHOOL_NJUPT(u'南京邮电大学',u'http://njupt.91job.gov.cn', u'/teachin?time=7')
	result_list.append(njupt)
	
	njust=SCHOOL_NJUST(u'南京理工大学',u'http://njust.91job.gov.cn', u'/teachin?time=7')
	result_list.append(njust)
	
	print add_serval_school_to_HTML_body(result_list)
