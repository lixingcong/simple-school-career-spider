## 简单爬虫

> Tested on Python 2.7.11

目前支持的学校：主要是江沪

- 南京大学
- 东南大学
- 南京理工大学
- 南京邮电大学
- 中国矿业大学
- 上海大学
- 上海交通大学

安装依赖

	sudo pip install beautifulsoup4
	sudo pip install lxml
	
运行(以南大为例)

	python schools/nju.py
	
编写合适的```main.py```和```my_mail_accounts.py```，可以实现抓取多个学校并发送到指定邮箱

	cd my_mail
	cp my_mail_accounts_example.py my_mail_accounts.py
	# 填入邮箱帐号
	vi my_mail_accounts.py

## TODO

编写继承```school_base```类，实现支持更多的学校。