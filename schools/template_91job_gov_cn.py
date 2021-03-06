#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年8月30日
@author: li

这个是91job.gov.cn网站模板，适用于江苏省大多数高校
'''
from bs4 import BeautifulSoup
from schools.school_base import SCHOOL_BASE
import datetime

class SCHOOL_91JOB_GOV_CN(SCHOOL_BASE):	
	def format_date(self, input_string, split_symbol):
		t = input_string
		if t[-2] == split_symbol:
			t = t[:-1] + '0' + t[-1]
		if t[-5] == split_symbol:
			t = t[:-4] + '0' + t[-4:]
		return t[5:]
		
				
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
				
				date_ = list_each_course[4].string[:10].strip()  # 日期
				if date_.startswith(u'201'):  # 2016, 2017....
					tmp_date = self.format_date(date_, '-')
					weekday_num = self.today.replace(month=int(tmp_date[:2]), day=int(tmp_date[-2:])).weekday()
					list_one.append(tmp_date + u'<br>周' + self.weekday[weekday_num])
				else:
					list_one.append(date_)
					
				list_one.append(list_each_course[4].string[10:].strip())  # 时间
				# if exists then add to dict
				if list_one[3] in self.dict_all.iterkeys():
					self.dict_all[list_one[3]].append(list_one)
				else:
					list_to_insert = []
					list_to_insert.append(list_one)
					self.dict_all[list_one[3]] = list_to_insert
				self.item_counter += 1
					
			self.recursive_get_next_page_content(res)
			
	def recursive_get_next_page_content(self, BeautifulSoup_obj):
		next_page = BeautifulSoup_obj.find('li', {'class':'next'})
		if next_page is not None:
			# 尾递归条件, class='next hidden'
			if len(list(next_page['class'])) == 2:
				return
			
			self.open_url_and_get_page(next_page.a['href'])
			self.recursive_get_each_entry()
					
	def convert_to_table(self):
		self.add_title_start_to_content()
		if self.dict_all == {}:
			self.content += u'<p>抓取内容为空</p>'
		else:
			self.add_table_start_to_content()
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
			self.add_table_end_to_content()
		self.add_title_end_to_content()
		
