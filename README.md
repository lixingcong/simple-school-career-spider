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
	
仅抓取一个学校(以南大为例)

	python schools/nju.py

## 投递邮件

逻辑是先抓取，生成HTML文件，然后调用类mail_account实现读取HTML文件，最后发送到邮箱

编写合适的```main.py```和```mail_account_private.py```，可以实现抓取多个学校并发送到指定邮箱

	cd my_mail
	# 创建一个mail_account类（继承mail_account_base）
	# 可以参考mail_account_example.py，比如添加一个新浪邮箱
	cp mail_account_example.py mail_account_private_sina.py
	vi mail_account_private_sina.py
	
	# 参考main_send_mail.py修改并创建一个新浪邮箱的对象
	cd ..
	vi main_send_mail.py
	
	# 抓取并发送邮件
	python main.py
	python main_send_mail.py

可以修改crontab实现定时投递

	vi /etc/crontab
	# 每天6点抓取，6点20分投递邮箱
	0 6 * * * root python /root/simple-school-career-spider/main.py
	20 6 * * * root python /root/simple-school-career-spider/main_send_mail.py

## 自定义

编写继承```mail_account_base```类，实现添加更多的邮箱与收件人。

编写继承```school_base```类，实现支持更多的学校。
