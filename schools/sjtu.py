#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月1日
@author: li
'''

from schools.school_base import SCHOOL_BASE
from bs4 import BeautifulSoup


class SCHOOL_SJTU(SCHOOL_BASE): 
	def __init__(self, isFromLocal=False):
		SCHOOL_BASE.__init__(self, u'上海交通大学', u'sjtu', u'http://www.job.sjtu.edu.cn', u'/eweb/jygl/zpfw.so?modcode=jygl_zpxxck&subsyscode=zpfw&type=searchZpxx&zpxxType=new', isFromLocal=isFromLocal)
	
	def recursive_get_each_entry(self):
		if self.content_original:
			res = BeautifulSoup(self.content_original, "html.parser")
			lis = res.select('.z_newsl li')

			for li in lis[1:]:
				list_one = []
				divs = list(li.find_all('div'))
				# company name + date
				list_one.append(divs[2].string[5:] + divs[0].a.string)
				# link
				fake_link = str(divs[1].a['onclick']).strip()
				list_one.append(self.get_real_link(fake_link))
				# job name
				list_one.append(divs[1].a.string.strip())

				# if company exists then add to dict
				if list_one[0] in self.dict_all.iterkeys():
					self.dict_all[list_one[0]].append(list_one)
				else:
					list_to_insert = []
					list_to_insert.append(list_one)
					self.dict_all[list_one[0]] = list_to_insert
				
				self.item_counter+=1
	
	def convert_to_table(self):
		self.add_title_to_content()
		if self.dict_all == {}:
			self.content += u'<p>抓取内容为空</p>'
		else:
			self.content += u'<table>'
			self.content += u'<tr><th>公司 发布日期</th><th>职位</th></tr>'
			for list1 in reversed(sorted(self.dict_all.iterkeys())):
				len1 = len(self.dict_all[list1])
				is_firstline = True
				self.content += u'<tr><th rowspan="' + str(len1) + u'">' + list1[5:] + u' ' + list1[:5] + u'</th>'
				for i in self.dict_all[list1]:
					if is_firstline == False:
						self.content += u'<tr>'
					self.content += u'<th><a href="' + self.host + i[1] + u'">' + i[2] + u'</a></tr>'
					is_firstline = False
			self.content += u'</table>'
		self.add_homepage_link_to_content()
	
	def get_real_link(self, input_string):
		# input string should be like this:
		# viewZpxx('PPaDGP38YQTscYHmhM3pWt', 'jygl_scfwyrdw')
		splited_str = input_string.split('\'')
		param_1 = splited_str[1]
		param_2 = splited_str[3]
		return u'/eweb/jygl/zpfw.so?modcode=' + param_2 + u'&subsyscode=zpfw&type=viewZpxx&id=' + param_1
			

		
if __name__ == '__main__':
	obj = SCHOOL_SJTU(isFromLocal=False)
	content = u'<html><head><meta charset="utf-8"><style>table, th, td { border: 1px solid #99cccc; text-align: left;}</style></head><body><h2>未来七日宣讲会</h2>'
	content += obj.get_HTML()
	content += u'<p>由<a href="http://lixingcong.github.io">Lixingcong</a>使用python强力驱动</p></body></html>' 
	print content	
	
