#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月2日
@author: li
'''
from schools.school_base import SCHOOL_BASE
from bs4 import BeautifulSoup
import requests

class SCHOOL_SCUT(SCHOOL_BASE):
	def __init__(self, isFromLocal=False):
		SCHOOL_BASE.__init__(self, u'华南理工大学', u'http://202.38.194.183', u'/jyzx/xs/zpxx/xyxj/', isFromLocal=isFromLocal)
		self.payload = {
			'pageNo':'1',
			'daoxv1':'-1',
			'time':'-14',  # 近两周
			'imageField':u'搜索',
			'pageNO':''  # 当前页码
		}
		
	def open_url_and_get_page(self, page=None):
		if self.isFromLocal is False:
			url = self.host + self.url
			if page is None:
				conn = requests.get(url, headers=self.header, timeout=60)
			else:
				self.payload['pageNO'] = page
				conn = requests.post(url, headers=self.header, timeout=60, data=self.payload)
			
			self.content_original = conn.content
		else:
			with open('/tmp/req.html', 'rb') as f:
				self.content_original = f.read().decode('utf-8')
		
	def recursive_get_each_entry(self):
		if self.content_original:
			res = BeautifulSoup(self.content_original, "html.parser")
			ul_original = res.find('div', {'class':'list'}).ul
			lis = ul_original.find_all('li')
			for li in lis:
				list_one = []
				date_and_time = li.div.string.strip().split()
				# date
				list_one.append(self.format_date(date_and_time[0], '-'))
				# time
				list_one.append(date_and_time[1])
				# link
				list_one.append(li.a['href'])
				# name
				list_one.append(li.a.string.strip())
				
				# if exists then add to dict
				if list_one[0] in self.dict_all.iterkeys():
					self.dict_all[list_one[0]].append(list_one)
				else:
					list_to_insert = []
					list_to_insert.append(list_one)
					self.dict_all[list_one[0]] = list_to_insert
					
			self.recursive_get_next_page_content(res)
					
	def recursive_get_next_page_content(self, BeautifulSoup_obj):
		next_page = BeautifulSoup_obj.find('a', {'class':'page-next'})
		if next_page is not None:
			page_number = next_page['href'].split('(')[1][:-2]
			self.open_url_and_get_page(page=page_number)
			self.recursive_get_each_entry()

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
					self.content += u'<th><a href="' + self.host + i[2] + u'">' + i[3] + u'</a></th>'
					self.content += u'<th>' + i[1] + u'</th></tr>'
					is_firstline = False
			self.content += u'</table>'
			
	def format_date(self, input_string, split_symbol):
		t = input_string
		if t[-2] == split_symbol:
			t = t[:-1] + '0' + t[-1]
		if t[-5] == split_symbol:
			t = t[:-4] + '0' + t[-4:]
		return t[5:]
	
if __name__ == '__main__':
	obj = SCHOOL_SCUT(False)
	content = u'<html><head><meta charset="utf-8"><style>table, th, td { border: 1px solid #99cccc; text-align: left;}</style></head><body><h2>未来七日宣讲会</h2>'
	content += obj.get_HTML()
	content += u'<p>由<a href="http://lixingcong.github.io">Lixingcong</a>使用python强力驱动</p></body></html>' 
	print content	
	
	
