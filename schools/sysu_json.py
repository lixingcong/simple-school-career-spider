#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月1日
@author: li
这个版本是适用于中大json版本的系统抓取，中大的网站某次使用json版的系统，抓取json比原来ASP方式简单多了
'''
from schools.school_base import SCHOOL_BASE
import datetime
import json

class SCHOOL_SYSU_JSON(SCHOOL_BASE):
	def __init__(self, isFromLocal=False):
		SCHOOL_BASE.__init__(self, u'中山大学', u'http://career.sysu.edu.cn', u'/pass/getListPassByType/%5B0%5D/1', isFromLocal=isFromLocal)
		self.json_obj = None
		
	def recursive_get_each_entry(self):
		if self.content_original:
			self.json_obj = json.loads(self.content_original, encoding='utf-8')
			
			today = datetime.datetime.today()
			
			for i in self.json_obj['passes']:
				date_tmp = self.get_json_key_value_safely(i,'date')
				if date_tmp == '?': # invalid
					continue
				
				hold_date, hold_time = self.format_time(date_tmp)
				hold_date_datetime_object = today.replace(month=int(hold_date[:2]), day=int(hold_date[-2:]))
				if hold_date_datetime_object < today:
					break
								
				list_one = []
				list_one.append(hold_date)  # date
				list_one.append(self.get_json_key_value_safely(i, 'title'))  # name
				list_one.append(self.get_json_key_value_safely(i, 'location', 'name'))  # loc
				list_one.append(hold_time)  # time
				list_one.append(self.get_json_key_value_safely(i, '_id'))  # link id
			
				# if exists then add to dict
				if list_one[0] in self.dict_all.iterkeys():  # if date exsit
					self.dict_all[list_one[0]].append(list_one)
				else:
					list_to_insert = []
					list_to_insert.append(list_one)
					self.dict_all[list_one[0]] = list_to_insert

				
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
					self.content += u'<th><a href="' + self.host + u'/#/passList/0?id=' + i[4] + u'">' + i[1] + u'</a></th>'
					self.content += u'<th>' + i[2] + u'</th>'
					self.content += u'<th>' + i[3] + u'</th></tr>'
					is_firstline = False
			self.content += u'</table>'
			
	def get_json_key_value_safely(self, json_obj, *json_key):
		result = json_obj
		
		# python args
		# http://stackoverflow.com/questions/3394835/args-and-kwargs
		for arg_count, arg in enumerate(json_key):
			try:
				result = result[arg]  # recursive search: exception was thrown when key-value was not found
			except:
				result = None
				break
			
		return result if result is not None else '?'

	
	def format_time(self, input_string):
		t = str(input_string[5:-8])
		t = t.split('T')
		UTC_plus_8 = str(int(t[1][:2]) + 8).zfill(2)  # UTC+8
		t[1] = UTC_plus_8 + t[1][-3:]
		return t
		
if __name__ == '__main__':
	obj = SCHOOL_SYSU_JSON(False)
	content = u'<html><head><meta charset="utf-8"><style>table, th, td { border: 1px solid #99cccc; text-align: left;}</style></head><body><h2>未来七日宣讲会</h2>'
	content += obj.get_HTML()
	content += u'<p>由<a href="http://lixingcong.github.io">Lixingcong</a>使用python强力驱动</p></body></html>'
	print content

