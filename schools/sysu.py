#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016年9月1日
@author: li
'''
from schools.school_base import SCHOOL_BASE
import requests
from bs4 import BeautifulSoup
import datetime

class SCHOOL_SYSU(SCHOOL_BASE):
	def __init__(self, isFromLocal=False):
		SCHOOL_BASE.__init__(self, u'中山大学', u'http://career.sysu.edu.cn', u'/Management_Field/Public/LectureManage.aspx', isFromLocal=isFromLocal)
		self.payload = {
			'__VIEWSTATEGENERATOR':'',
			'__VIEWSTATE': '',
			'__EVENTVALIDATION': '',
			'__ASYNCPOST': 'true',
			'__EVENTTARGET': '',
			'__EVENTARGUMENT': ''
		}
		
	def open_url_and_get_page(self):
		if self.isFromLocal is False:
			conn = requests.get(self.host+self.url, headers=self.header, timeout=60)
			res = BeautifulSoup(conn.content, "html.parser")			

			self.payload["__EVENTVALIDATION"] = res.select("#__EVENTVALIDATION")[0]["value"]
			self.payload["__VIEWSTATEGENERATOR"] = res.select("#__VIEWSTATEGENERATOR")[0]["value"]
			self.payload["__VIEWSTATE"] = res.select("#__VIEWSTATE")[0]["value"]

			# update URL assigned by ASP.Net
			self.url = conn.url
			self.content_original = conn.content
		else:
			with open('/tmp/req.html', 'rb') as f:
				self.content_original = f.read().decode('utf-8')
	
	def recursive_get_each_entry(self):
		if self.content_original:
			res = BeautifulSoup(self.content_original, "html.parser")
			table_original = res.find('table', {'class':'grid pager'})
			
			today=datetime.datetime.today()
			trs = table_original.find_all('tr')
			for tr in trs[3:]:
				list_one = []
				tds = list(tr.find_all('td'))
				date_and_time=tds[1].span.string.strip().split()
				# date comparasion
				# http://stackoverflow.com/questions/1831410/python-time-comparison
				hold_date=self.format_date(date_and_time[0],'/')
				hold_date_datetime_object=today.replace(month=int(hold_date[:2]),day=int(hold_date[-2:]))
				if hold_date_datetime_object<today:
					break
				# time
				print self.format_time(date_and_time[1],':')
				
				# fake link, TODO
				print tds[0].a['href']
				# job name
				print tds[0].a.string.strip()
				# location
				print tds[2].span.string.strip()
				
				

	def get_real_link(self, input_string):
		# input string should be like this:
		# javascript:__doPostBack('ctl00$ContentPlaceHolder1$GridView1$ctl03$hplAction','')
		splited_str = input_string.split('\'')
		print splited_str
		
	def format_date(self, input_string, split_symbol):
		t = input_string
		if t[-2] == split_symbol:
			t = t[:-1] + '0' + t[-1]
		if t[-5] == split_symbol:
			t = t[:-4] + '0' + t[-4:]
		return t[5:]
	
	def format_time(self, input_string, split_symbol):
		return input_string[:-3]
		
if __name__ == '__main__':
	obj=SCHOOL_SYSU(True)
	obj.open_url_and_get_page()
	obj.recursive_get_each_entry()



'''
中大的网站我花了很长时间调试

使用chrome的F12，Network标签下勾选"Preserve Log"以保存redirect前的结果，还有禁用cache。

发觉中大的先是在点击条目后进行POST，此时post的地址是新的URL，注意及时更换

self.url = conn.url

与post有关的payload为
payload = {
	'__VIEWSTATEGENERATOR':'',
	'__VIEWSTATE': '',
	'__EVENTVALIDATION': '',
	'__ASYNCPOST': 'true',
	'__EVENTTARGET': '', #这个是a标签的href第一个参数
	'__EVENTARGUMENT': '',
}

服务器使用ASP.Net，收到来自客户的post后，返回一个redirect的结果重定向为正确的页面

print res.content
结果
69|dataItem||<script type="text/javascript">window.location="about:blank"</script>|79|pageRedirect||/(S(z2rutgrcb4piw335ifieiwzd))/Management_Field/Public/ViewLecture.aspx?id=5734

提取最后的地址，去掉Sxxxxx的会话id，就是正确的地址
'''