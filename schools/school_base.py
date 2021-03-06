#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import datetime

class SCHOOL_BASE(object):
	def __init__(self, title, abbr, host, url, isFromLocal=False):
		self.title = title
		self.abbr = abbr
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
		self.item_counter = 0
		self.today = datetime.datetime.today()
		self.weekday = [u'一', u'二', u'三', u'四', u'五', u'六', u'日']
		
	def open_url_and_get_page(self, link=None):
		# open page and it should be decoded here
		if self.isFromLocal is False:
			if link is None:
				url = self.host + self.url
			else:
				url = self.host + link
			
			conn = requests.get(url, headers=self.header, timeout=60)
			self.content_original = conn.content
		else:
			with open('/tmp/req.html', 'rb') as f:
				self.content_original = f.read().decode('utf-8')
	
	def recursive_get_each_entry(self):
		# get each page and add to self.content
		pass
	
	def recursive_get_next_page_content(self, BeautifulSoup_obj):
		# get next page from a bs4 object
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
	
	def get_title(self):
		return self.title
	
	def get_item_counter(self):
		return str(self.item_counter)
	
	def get_school_abbreviation(self):
		return self.abbr
	
	def add_title_start_to_content(self):
		self.content += (u'<h3>' + self.title + u'</h3>')
		
	def add_title_end_to_content(self):
		self.content += u'<p><a href="#">回到首页</a></p>'
		
	def add_table_start_to_content(self):
		self.content += u'<div id="' + self.abbr + u'" class="school"><table>'
		
	def add_table_end_to_content(self):
		self.content += u'</table></div>'
