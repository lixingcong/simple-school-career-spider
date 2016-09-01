#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年8月30日
@author: li
'''
from bs4 import BeautifulSoup
from schools.school_base import SCHOOL_BASE

class SCHOOL_CUMT(SCHOOL_BASE):
			
	def format_time(self, input_string, split_symbol):
		t = input_string
		if t[-2] == split_symbol:
			t = t[:-1] + '0' + t[-1]
		if t[-5] == split_symbol:
			t = t[:-4] + '0' + t[-4:]
		return t
		
				
	def recursive_get_each_entry(self):
		if self.content_original:
			res = BeautifulSoup(self.content_original, "html.parser")
			list1 = res.find_all('ul', {'class':'infoList teachinList'})
			for i in list1:
				fuck = BeautifulSoup(str(i), 'lxml')
				list_each_course = list(fuck.find_all('li'))
				list_one = []
				list_one.append(list_each_course[0].a['href'].strip())  # 链接
				list_one.append(list_each_course[0].a.string.strip())  # 企业名
				list_one.append(list_each_course[3].string.strip())  # 公教地点
				date_ = (list_each_course[4].string[:10].strip())  # 日期
				list_one.append(self.format_time(date_, '-'))
				list_one.append(list_each_course[4].string[10:].strip())  # 时间
				# if exists then add to dict
				if list_one[3] in self.dict_all.iterkeys():
					self.dict_all[list_one[3]].append(list_one)
				else:
					list_to_insert = []
					list_to_insert.append(list_one)
					self.dict_all[list_one[3]] = list_to_insert
					
	def convert_to_table(self):
		self.content += (u'<h3>' + self.title + u'</h3>')
		if self.dict_all == {}:
			self.content += u'<p>抓取内容为空</p>'
		else:
			self.content += u'<table>'
			for list1 in sorted(self.dict_all.iterkeys()):
				len1 = len(self.dict_all[list1])
				is_firstline = True
				self.content += u'<tr><th rowspan="' + str(len1) + u'">' + list1 + u'</th>'
				for i in self.dict_all[list1]:
					if is_firstline == False:
						self.content += u'<tr>'
					self.content += u'<th><a href="' + self.host + i[0] + u'">' + i[1] + u'</a></th>'
					self.content += u'<th>' + i[2] + u'</th>'
					self.content += u'<th>' + i[4] + u'</th></tr>'
					is_firstline = False
			self.content += u'</table>'
		
if __name__ == '__main__':
	c = SCHOOL_CUMT(u"中国矿业大学", u'http://jyzd.cumt.edu.cn', u'/teachin?time=14', isFromLocal=False)		
	content = u'<html><head><meta charset="utf-8"><style>table, th, td { border: 1px solid #99cccc; text-align: left;}</style></head><body><h2>未来七日宣讲会</h2>'
	content += c.get_HTML()
	content += u'<p>由<a href="http://lixingcong.github.io">Lixingcong</a>使用python强力驱动</p></body></html>' 
	print content
