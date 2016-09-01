#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月1日
@author: li
'''
from schools.cumt import SCHOOL_CUMT

class SCHOOL_SEU(SCHOOL_CUMT):
	pass

if __name__ == '__main__':
	c = SCHOOL_SEU(u"东南大学", u'http://seu.91job.gov.cn', u'/teachin?time=14', isFromLocal=False)		
	content = u'<html><head><meta charset="utf-8"><style>table, th, td { border: 1px solid #99cccc; text-align: left;}</style></head><body><h2>未来七日宣讲会</h2>'
	content += c.get_HTML()
	content += u'<p>由<a href="http://lixingcong.github.io">Lixingcong</a>使用python强力驱动</p></body></html>' 
	print content	