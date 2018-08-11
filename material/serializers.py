from rest_framework import serializers
from .models import *


class ImageSerializers(serializers.ModelSerializer):
	""" 图片 """
	class Meta(object):
		model = Image
		fields = ('iuid', 'user', 'titile', 'path', 'create_time')


class ArticleSerializers(serializers.ModelSerializer):
	""" 文章 """
	class Meta(object):
		model = Article
		fields = ('vuid', 'user', 'titile', 'content', 'create_time')


class VideoSerializers(serializers.ModelSerializer):
	""" 视频 """
	class Meta(object):
		model = Video
		fields = ('vuid', 'user', 'titile', 'path', 'create_time')

