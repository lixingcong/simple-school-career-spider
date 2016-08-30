#!/usr/bin/env python
# -*- coding: utf-8 -*-



class SCHOOL_BASE(object):
	def __init__(self, title, host, url, encode=None, isFromLocal=False):
		self.title = title
		self.host = host
		self.url = url
		self.encode = encode
		self.content_original = ''
		self.content = ''
		self.header = {'User-Agent':u'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
          'Referer':self.host
          }
		self.isFromLocal = isFromLocal
		self.dict_all = {}
		
	def open_url_and_get_page(self):
		# open page and it should be decoded here
		pass
	
	def recursive_get_each_entry(self):
		# get each page and add to self.content
		pass
	
	def format_date(self, input_string, split_symbol):
		# format data to MM:DD HH:MM:SS
		pass
	
	def convert_to_table(self):
		# merge content to a table with label <td> 
		pass
	
	def get_HTML(self):
		# return processed HTML content
		return self.content
	
	
		
