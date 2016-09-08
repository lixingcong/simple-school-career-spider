#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年8月30日
@author: li
'''
from schools.sysu import SCHOOL_SYSU
from schools.scut import SCHOOL_SCUT

def add_serval_school_to_HTML_body(input_school_list, HTML_title):
	if input_school_list is not None:
		content = u'<html><head><meta charset="utf-8"><style>table, th, td { border: 1px solid #99cccc; text-align: left;}</style></head><body><h2>' + HTML_title + u'</h2>'
		import time
		content += u'<p>更新时间：' + time.strftime("%Y-%m-%d %H:%M") + u'</p>'
		for i in input_school_list:
			try:
				content += i.get_HTML()
			except:
				content += u'<p>' + i.get_title() + u': error occurs</p>'
		content += u'<p>由<a href="http://lixingcong.github.io">Lixingcong</a>使用python强力驱动。Github仓库：<a href="https://github.com/lixingcong/simple-school-career-spider">simple-school-career-spider</a></p></body></html>' 
		return content
	return None
	
if __name__ == '__main__':
	school_list = []
	# TODO: 多线程抓取，重写add_serval_school_toHTML函数
	
	school_list.append(SCHOOL_SYSU())
	school_list.append(SCHOOL_SCUT())
	
	# Save content to local disk
	with open('/tmp/Guangzhou_spider.html', 'wb') as f:
		f.write(add_serval_school_to_HTML_body(school_list, u'未来两周宣讲会').encode('utf-8'))
