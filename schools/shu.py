#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月1日
@author: li
'''
from schools.school_base import SCHOOL_BASE
import requests
from bs4 import BeautifulSoup
import re

class SCHOOL_SHU(SCHOOL_BASE):
	def __init__(self, isFromLocal=False):
		SCHOOL_BASE.__init__(self, u'上海大学', u'shu', u'http://zbb.shu.edu.cn', u'http://zbb.shu.edu.cn/PositionList.aspx', isFromLocal=isFromLocal)
		self.header['X-MicrosoftAjax'] = 'Delta=true'
		self.header['X-Requested-With'] = 'XMLHttpRequest'
		self.payload = {
			'__VIEWSTATEGENERATOR':'',
			'__VIEWSTATE': '',
			'__EVENTVALIDATION': '',
			'ctl00$content$ddlXL':u'本科',
			'ctl00$content$ddlJobNature':u'全职',
			'ctl00$content$ddlReleaseDate':'7',
			'ctl00$content$btnSearch':u'职位搜索',
			'ctl00$content$ddlReleaseDate':'1',  # 一天内
			'__EVENTTARGET':'',
			'ctl00$content$gvPosiList$ctl01$txtNewPageIndex':'',
		}
		self.isPopped = False
		self.viewstate = ''
		self.eventvalidation = ''
		self.re_program_viewstate = re.compile("__VIEWSTATE\|.*?\|")
		self.re_program_eventvalidation = re.compile("__EVENTVALIDATION\|.*?\|")
		
		
	def open_url_and_get_page(self, thispage=None):
		if self.isFromLocal is False:			
			if thispage is None:
				conn = requests.get(self.url, headers=self.header, timeout=60)
				res = BeautifulSoup(conn.content, "html.parser")
				ev = res.select("#__EVENTVALIDATION")[0]["value"]
				vs = res.select("#__VIEWSTATE")[0]["value"]
				vsg = res.select("#__VIEWSTATEGENERATOR")[0]["value"]				
				self.payload["__VIEWSTATEGENERATOR"] = vsg
				self.payload["__EVENTVALIDATION"] = ev
				self.payload["__VIEWSTATE"] = vs
			else:
				self.find_real_VIEWSTATE_and_EVENTVALIDATION()
				self.payload["__EVENTVALIDATION"] = self.eventvalidation
				self.payload["__VIEWSTATE"] = self.viewstate
				self.payload['ctl00$content$gvPosiList$ctl01$txtNewPageIndex'] = thispage
				
			conn = requests.post(self.url, headers=self.header, timeout=60, data=self.payload)
			
			if self.isPopped is False:
				self.payload.pop('ctl00$content$btnSearch')
				self.payload['__EVENTTARGET'] = 'ctl00$content$gvPosiList$ctl01$btnNext'
				self.isPopped = True
				
			self.content_original = conn.content
			
		else:
			with open('/tmp/req.html', 'rb') as f:
				self.content_original = f.read().decode('utf-8')
		
	
	def recursive_get_each_entry(self):
		if self.content_original:
			res = BeautifulSoup(self.content_original, "html.parser")
			table_original = res.find('table', {'class':'table table-striped table-bordered'})

			if table_original:
				trs = table_original.find_all('tr')
				for tr in trs[3:]:
					list_one = []
					tds = list(tr.find_all('td'))
					# company name + publish date
					list_one.append(tds[5].string.strip() + tds[2].string.strip())
					# link
					list_one.append(tds[0].a['href'].strip())
					# link string
					list_one.append(tds[0].a.string.strip())
					# quantity
					list_one.append(tds[4].string.strip())
					
					# if exists then add to dict
					if list_one[0] in self.dict_all.iterkeys():  # if company exsit
						self.dict_all[list_one[0]].append(list_one)
					else:
						list_to_insert = []
						list_to_insert.append(list_one)
						self.dict_all[list_one[0]] = list_to_insert
						
					self.item_counter += 1
					
				self.recursive_get_next_page_content(res)
	
	def recursive_get_next_page_content(self, BeautifulSoup_obj):
		this_page = BeautifulSoup_obj.select("#content_gvPosiList_lblPageIndex")[0].string
		max_page = BeautifulSoup_obj.select("#content_gvPosiList_lblPageCount")[0].string
		if int(this_page) < int(max_page):
			self.open_url_and_get_page(this_page)
			self.recursive_get_each_entry()
			
	
	def convert_to_table(self):
		self.add_title_start_to_content()
		if self.dict_all == {}:
			self.content += u'<p>抓取内容为空</p>'
		else:
			self.content += u'<table>'
			self.content += u'<tr><th>公司 发布日期</th><th>职位（学历：本科）</th><th>人数</th></tr>'
			for list1 in reversed(sorted(self.dict_all.iterkeys())):
				len1 = len(self.dict_all[list1])
				is_firstline = True
				self.content += u'<tr><th rowspan="' + str(len1) + u'">' + list1[10:] + u' ' + list1[5:10] + u'</th>'
				for i in self.dict_all[list1]:
					if is_firstline == False:
						self.content += u'<tr>'
					self.content += u'<th><a href="' + self.host + i[1][1:] + u'">' + i[2] + u'</a></th>'
					self.content += u'<th>' + i[3] + u'</th></tr>'
					is_firstline = False
			self.content += u'</table>'
		self.add_title_end_to_content()
			
	def find_real_VIEWSTATE_and_EVENTVALIDATION(self):
		self.viewstate = self.re_program_viewstate.findall(self.content_original)[0][12:-1]
		self.eventvalidation = self.re_program_eventvalidation.findall(self.content_original)[0][18:-1]
		
	
if __name__ == '__main__':
	obj = SCHOOL_SHU()
	content = u'<html><head><meta charset="utf-8"><style>table, th, td { border: 1px solid #99cccc; text-align: left;}</style></head><body><h2>未来七日宣讲会</h2>'
	content += obj.get_HTML()
	content += u'<p>由<a href="http://lixingcong.github.io">Lixingcong</a>使用python强力驱动</p></body></html>'
	print content

'''
上海大学的ASP.net提交post非常蛋疼，那个VIEWSTATE和EVENTVALIDATION是动态更新的，需要写一个正则匹配找出每页的正确值
作为data-payload进行提交表单POST才能有结果
'''
	
