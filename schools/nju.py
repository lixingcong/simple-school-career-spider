#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月1日
@author: li
注意：南京大学的端口是9081，自己服务器防火墙需要打开这个入站请求才能完成
'''
from bs4 import BeautifulSoup
import requests
from schools.school_base import SCHOOL_BASE

class SCHOOL_NJU(SCHOOL_BASE):
	def __init__(self, isFromLocal=False):
		SCHOOL_BASE.__init__(self, u'南京大学', u'nju', u'http://job.nju.edu.cn:9081', u'', isFromLocal=isFromLocal)
		self.begin_date = ''
		self.end_date = ''
		
	def open_url_and_get_page(self, link=None):
		# open page and it should be decoded here
		if self.isFromLocal is False:
			if link is None:
				self.calc_delta_date()
				url = u'/login/nju/home.jsp?type=zph&pageNow=1&sfss=sfss&zphzt=&jbksrq=' + self.begin_date + u'&jbjsrq=' + self.end_date + u'&sfgq=&pageSearch=1'
			else:
				url = u'/login/nju/' + link
			
			conn = requests.get(self.host + url, headers=self.header, timeout=60)
			self.content_original = conn.content
		else:
			with open('/tmp/req.html', 'rb') as f:
				self.content_original = f.read().decode('utf-8')
	
	def recursive_get_each_entry(self):
		if self.content_original:
			res = BeautifulSoup(self.content_original, "html.parser")
			res_links = res.find_all('span', {'class':'article'})
			
			try:
				res_positions = res.find_all('span', {'style':'float:right'})
			except Exception,e:
				print e
				return None
			
			if res_positions:
				index = 0
				for res_link in res_links:
					list_one = []
					list_one.append(res_link.a['href'].strip())  # link
					list_one.append(res_link.a.string.strip())  # name
					tmp_strings = res_positions[index].string.split()
					list_one.append(tmp_strings[0])  # location
					
					date_ = (tmp_strings[1])  # date
					if date_.startswith(u'201'):  # 2016  2017 ...
						list_one.append(self.format_date(date_, '-'))
					else:
						list_one.append(date_)
						
					list_one.append(tmp_strings[2])  # time				
					
					# if exists then add to dict
					if list_one[3] in self.dict_all.iterkeys():
						self.dict_all[list_one[3]].append(list_one)
					else:
						list_to_insert = []
						list_to_insert.append(list_one)
						self.dict_all[list_one[3]] = list_to_insert
					
					index += 1
				
				self.item_counter += index
				
				# 递归抓取
				self.recursive_get_next_page_content(res)
			
	def recursive_get_next_page_content(self, BeautifulSoup_obj):
		nav_links = BeautifulSoup_obj.find_all('a', {'style':'width:50px;color:#0082e7;'})
		for link in nav_links:
			if link.string == u'下一页':
				self.open_url_and_get_page(link['href'])
				self.recursive_get_each_entry()
					
	def convert_to_table(self):
		self.add_title_to_content()
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
					self.content += u'<th><a href="' + self.host + u'/login/nju/' + i[0] + u'">' + i[1] + u'</a></th>'
					self.content += u'<th>' + i[2] + u'</th>'
					self.content += u'<th>' + i[4] + u'</th></tr>'
					is_firstline = False
			self.content += u'</table>'
		self.add_homepage_link_to_content()
		
	def format_date(self, input_string, split_symbol):
		t = input_string
		if t[-2] == split_symbol:
			t = t[:-1] + '0' + t[-1]
		if t[-5] == split_symbol:
			t = t[:-4] + '0' + t[-4:]
		return t[5:]
			
	
	def calc_delta_date(self):
		from datetime import datetime, timedelta  		
		now = datetime.now()  
		now_delta_10days = now + timedelta(days=14)
		yesterday = now - timedelta(days=1)
		self.end_date = now_delta_10days.strftime("%Y-%m-%d")
		self.begin_date = yesterday.strftime("%Y-%m-%d")
		
		
if __name__ == '__main__':
	obj = SCHOOL_NJU(isFromLocal=False)
	content = u'<html><head><meta charset="utf-8"><style>table, th, td { border: 1px solid #99cccc; text-align: left;}</style></head><body><h2>未来七日宣讲会</h2>'
	content += obj.get_HTML()
	content += u'<p>由<a href="http://lixingcong.github.io">Lixingcong</a>使用python强力驱动。Github仓库：<a href="https://github.com/lixingcong/simple-school-career-spider">simple-school-career-spider</a></p></body></html>' 
	print content
	
	
