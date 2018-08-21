# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from uuid import uuid4
# Create your models here.
from User.models import MyUser
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Image(models.Model):
	""" 
	图片文件 
	"""
	iuid = models.UUIDField(default=uuid4())
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='图片发布者')
	titile = models.CharField(max_length=25, null=True, verbose_name='图片标题')
	path = models.ImageField(upload_to='static/img', default=None, verbose_name='图片路径')
	create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

	class Meta(object):
		db_table = 'image'
		verbose_name = verbose_name_plural = '图片'


class Video(models.Model):
	""" 
	视频文件 
	"""
	vuid = models.UUIDField(default=uuid4())
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='图片发布者')
	titile = models.CharField(max_length=25, null=True, verbose_name='图片标题')
	path = models.FileField(upload_to='static/video', default=None, verbose_name='图片路径')
	create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

	class Meta(object):
		db_table = 'video'
		verbose_name = verbose_name_plural = '视频'


class Article(models.Model):
	""" 
	文本文件 
	"""
	vuid = models.UUIDField(default=uuid4())
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='图片发布者')
	titile = models.CharField(max_length=25, null=True, verbose_name='图片标题')
	content = models.TextField(verbose_name='文章')
	create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

	class Meta(object):
		db_table = 'article'
		verbose_name = verbose_name_plural = '文章'


class Comment(models.Model):
	"""
	评论记录
	"""
	puid = models.UUIDField(default=uuid4())
	# 评论的类型
	ptype = models.IntegerField(verbose_name='评论的类型')
	# 评论的文件
	fileuid = models.CharField(max_length=50, verbose_name='评论的文件')
	# 评论的人
	commter = models.ForeignKey(MyUser, verbose_name='评论的人', on_delete=None)
	# 评论内容
	contnet = models.CharField(max_length=150, verbose_name='评论的内容')
	# 评论的时间
	create_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)

	class Meta(object):
		db_table = 'comment'
		verbose_name = "评论表"



