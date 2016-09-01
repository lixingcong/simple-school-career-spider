#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年8月30日
@author: li
'''
from schools.template_91job_gov_cn import SCHOOL_91JOB_GOV_CN
from schools.sysu import SCHOOL_SYSU
from schools.scut import SCHOOL_SCUT
from my_mail.send_mail import send_email


def add_serval_school_to_HTML_body(input_school_list):
	if input_school_list is not None:
		content = u'<html><head><meta charset="utf-8"><style>table, th, td { border: 1px solid #99cccc; text-align: left;}</style></head><body><h2>未来七日宣讲会</h2>'
		import time
		content += u'<p>发送时间：' + time.strftime("%Y-%m-%d %H:%M") + u'</p>'
		for i in input_school_list:
			content += i.get_HTML()
		content += u'<p>由<a href="http://lixingcong.github.io">Lixingcong</a>使用python强力驱动。Github仓库：<a href="https://github.com/lixingcong/simple-school-career-spider">simple-school-career-spider</a></p></body></html>' 
		return content
	return None
	
if __name__ == '__main__':
	school_list = []
	# TODO: 多线程抓取，重写add_serval_school_toHTML函数
	
	school_list.append(SCHOOL_SYSU())
	school_list.append(SCHOOL_SCUT())
	
	with open('/tmp/GuangZhou_spider.html','wb') as f:
		f.write(add_serval_school_to_HTML_body(school_list).encode('utf-8'))
