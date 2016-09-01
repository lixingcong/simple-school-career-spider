#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月1日
@author: li
'''
from schools.template_91job_gov_cn import SCHOOL_91JOB_GOV_CN

class SCHOOL_CUMT(SCHOOL_91JOB_GOV_CN):
	def __init__(self, isFromLocal=False):
		SCHOOL_91JOB_GOV_CN.__init__(self,u"中国矿业大学", u'http://jyzd.cumt.edu.cn', u'/teachin?time=14', isFromLocal=isFromLocal)

if __name__ == '__main__':
	c = SCHOOL_CUMT(isFromLocal=False)		
	content = u'<html><head><meta charset="utf-8"><style>table, th, td { border: 1px solid #99cccc; text-align: left;}</style></head><body><h2>未来七日宣讲会</h2>'
	content += c.get_HTML()
	content += u'<p>由<a href="http://lixingcong.github.io">Lixingcong</a>使用python强力驱动</p></body></html>' 
	print content
