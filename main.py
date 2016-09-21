#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年8月30日
@author: li
'''
from schools.sysu import SCHOOL_SYSU
from schools.scut import SCHOOL_SCUT
import time

def add_serval_school_to_HTML_body(input_school_list, HTML_title):
	if input_school_list is not None:
		school_content = u''
		
		# begin of HTML
		content = u'<html><head><meta charset="utf-8"><script hhh="lxc"></script>'		
		# CSS style
		content += u'<style>table, th, td { border: 1px solid #99cccc; text-align: left;}h3 { background: #99ccff; text-indent:0.6em}</style>'
		# begin of body
		content += u'</head><body onload="myload();">'
		# title
		content += u'<h2>' + HTML_title + u'</h2>'
		# update time
		content += u'<p>更新时间：' + time.strftime("%Y-%m-%d %H:%M") + u'</p>'
		# footer
		content += u'<p>由<a href="http://lixingcong.github.io">Lixingcong</a>使用python强力驱动。本自动爬虫程序已开源：<a href="https://github.com/lixingcong/simple-school-career-spider">simple-school-career-spider</a>，支持邮件自动投递</p>'		
		# build a navigator table link
		content += u'<h3>首页导航</h3><table><tr><th>选择</th><th>学校</th><th>招聘信息</th></tr>'
		for i in input_school_list:
			try:
				school_content += i.get_HTML()
				# Homepage Navigator
				content += u'<tr><th><input type="checkbox" id="_' + i.get_school_abbreviation() + u'" onclick="doPostBack(this);"></th><th>' + i.get_title() + u'</th><th>' + i.get_item_counter() + u'</th></tr>'
			except Exception, exc:
				school_content += u'<p style="background: #ff6666">' + i.get_title() + u': error occurs</p>'
				content += u'<tr><th>' + i.get_title() + u'</th><th>出错</th></tr>'
				print i.get_title(), exc
				
		# end of navigator table link		
		content += u'</table>'
		
		# school details
		content += school_content
		# end of HTML
		content += u'</body></html>' 
		
		return content
	
	# invalid school list
	return u'None'
	
if __name__ == '__main__':
	school_list = []
	# TODO: 多线程抓取，重写add_serval_school_toHTML函数
	
	school_list.append(SCHOOL_SYSU())
	school_list.append(SCHOOL_SCUT())
	
	# Save content to local disk
	with open('/tmp/Guangzhou_spider.html', 'wb') as f:
		f.write(add_serval_school_to_HTML_body(school_list, u'未来两周宣讲会').encode('utf-8'))
