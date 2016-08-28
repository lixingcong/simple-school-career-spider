#!/usr/bin/env python
# -*- coding: utf-8 -*-

class school_base(object):
	def __init__(self,title,host,url,encode=None):
		self.title=title
		self.host=host
		self.url=url
		self.encode=encode
		self.content=''
		
	def open_url_and_get_page(self):
		# open page and it should be decoded here
		pass
	
	def recursive_get_each_entry(self):
		# get each page and add to self.content
		pass
	
	def format_date(self,input_string):
		# format data to MM:DD HH:MM:SS
		pass
	
	def convert_to_table(self):
		# merge content to a table with label <td> 
		pass
	
	def get_HTML(self):
		# return processed HTML content
		pass
	
	
		