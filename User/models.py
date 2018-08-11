# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from uuid import uuid4
from django.contrib.auth.models import UserManager

# Create your models here.

# 用户性别
MALE = 1
FEMALE = 0

GENDER = (
    (MALE, '男'),
    (FEMALE, '女'),
)

# 用户状态
NOTACTIVE = 0
ACTIVATED = 1
BLOCKED = 2

USERSTATUS = (
    (NOTACTIVE, '未激活'),
    (ACTIVATED, '已激活'),
    (BLOCKED, '封锁'),
)


class MyUser(AbstractBaseUser):
	""" 用户表 """

	uuid = models.UUIDField(default=uuid4())
	nick = models.CharField(verbose_name='昵称', max_length=25, )
	gender = models.IntegerField(verbose_name='性别', choices=GENDER, blank=True, null=True)

	mobile = models.CharField(verbose_name='手机号', max_length=20,
								blank=True, null=True, unique=True)
	status = models.IntegerField(verbose_name='状态', choices=USERSTATUS,
								default=ACTIVATED)
	# psddword = models.CharField(max_length=128,verbose_name='密码', REQUIRED_FIELDS='True')
	province = models.CharField(verbose_name='省', max_length=12,
								blank=True, null=True)
	city = models.CharField(verbose_name='市', max_length=12,
								blank=True, null=True)
	district = models.CharField(verbose_name='区/县', max_length=12,
								blank=True, null=True)
	address = models.CharField(verbose_name='地址', max_length=200,
							   blank=True, null=True)
	login_ip = models.CharField(verbose_name='登录 IP', max_length=15,
								blank=True, null=True)
	origin = models.CharField(verbose_name='来源', max_length=20, blank=True,
							  null=True)
	create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

	USERNAME_FIELD = 'mobile'

	objects = UserManager()


class UserManager(BaseUserManager):
	def create_user(self):
		# TODO 权限
		pass

	def create_superuser(self):
		# TODO 超级用户
		pass
