#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

class SCHOOL_BASE(object):
	def __init__(self, title, host, url, isFromLocal=False):
		self.title = title
		self.host = host
		self.url = url
		self.content_original = ''
		self.content = ''
		self.header = {
			'User-Agent':u'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
			'Referer':self.host,
			'Accept-Language':u'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4'
		}
		self.isFromLocal = isFromLocal
		self.dict_all = {}
		
	def open_url_and_get_page(self):
		# open page and it should be decoded here
		if self.isFromLocal is False:
			conn = requests.get(self.host + self.url, headers=self.header)
			self.content_original = conn.content
		else:
			with open('/tmp/req.html', 'rb') as f:
				self.content_original = f.read().decode('utf-8')
		pass
	
	def recursive_get_each_entry(self):
		# get each page and add to self.content
		pass
	
	def format_time(self, input_string, split_symbol):
		# format time to HH:MM
		pass
	
	def format_date(self, input_string, split_symbol):
		# format data to YYYY-MM-DD
		pass
	
	def convert_to_table(self):
		# merge content to a table with label <td> 
		pass
	
	def get_HTML(self):
		# return processed HTML content
		self.open_url_and_get_page()
		self.recursive_get_each_entry()
		self.convert_to_table()
		return self.content
	
	
		
