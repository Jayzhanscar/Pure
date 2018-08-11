from rest_framework import serializers
from .models import MyUser


class UserRegisterSerializer(serializers.ModelSerializer):
	""" 用户名字序列化 """
	class Meta(object):
		model = MyUser
		fields = ('mobile', 'password')