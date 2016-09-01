## 简单爬虫

> Tested on Python 2.7.11

目前支持的学校

主要是苏沪广

- 南京大学
- 东南大学
- 南京理工大学
- 南京邮电大学
- 中国矿业大学
- 上海大学
- 上海交通大学
- 中山大学
- 华南理工大学

## 例子

添加环境变量

	vi ~/.bashrc
	export PYTHONPATH=.:$PYTHONPATH

使环境变量立即生效

	source ~/.bashrc

安装依赖

	sudo pip install beautifulsoup4
	sudo pip install lxml
	sudo pip install requests
	
单学校运行(以南大为例)

	python schools/nju.py

## 投递邮件

编写合适的```main.py```和```my_mail_accounts.py```，可以实现抓取多个学校并发送到指定邮箱

	cd my_mail
	cp my_mail_accounts_example.py my_mail_accounts.py
	# 填入邮箱帐号
	vi my_mail_accounts.py
	# 发送和邮件
	python main.py
	python main_send_mail.py

可以修改crontab支持定时投递

## TODO

编写继承```school_base```类，实现支持更多的学校。
