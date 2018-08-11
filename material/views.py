# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from .serializers import *
from django.shortcuts import render
from .models import Image
from rest_framework import status
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.core.cache import cache
import this
from rest_framework.response import Response
# Create your views here.


class ImgGet(APIView):
	""" 图片视图 """
	serializer_class = ImageSerializers

	def get(self, request, *args, **kwargs):
		""" 图片详情页面"""
		iuid = request.data.get('iuid')
		if not iuid:
			return Response({'data': 0, 'error': 'not found'})
		img = Image.objects.filter(iuid=iuid)
		data = ImageSerializers(img).data
		return Response(data=data, status=status.HTTP_200_OK)

	def post(self, request, *args, **kwargs):
		""" 提交图片 """
		uuid = request.COOKIES['uuid']
		user = MyUser.objects.filter(uuid=uuid)[0]
		imgae = Image()
		imgae.user = user
		imgae.path = request.data['file']
		imgae.titile = request.data['title']
		imgae.save()
		if not request.data:
			raise 'no'
		img = Image()
		return Response({'data': 1})


class VideoGet(APIView):
	""" 视频操作"""
	serializer_class = VideoSerializers

	def get(self, request, *args, **kwargs):
		""" 视频详情页"""
		vuid = request.data.get('vuid')
		if not vuid:
			return Response({'data': 0, 'error': 'not found'})
		vid = Video.objects.filter(vuid=vuid)
		data = VideoSerializers(vid).data
		return Response(data=data, status=status.HTTP_200_OK)

	def post(self, request, *args, **kwargs):
		""" 上传视频 """
		uuid = request.COOKIES['uuid']
		user = MyUser.objects.filter(uuid=uuid)[0]
		video = Video()
		video.user = user
		video.path = request.data['file']
		video.titile = request.data['title']
		video.save()
		if not request.data:
			raise 'no'
		return Response({'data': 1})


class ArticleGet(APIView):
	""" 文章 """
	serializer_class = ArticleSerializers

	def get(self, request, *args, **kwargs):
		""" 文章详情 """
		auid = request.data.get('auid')
		if not auid:
			return Response({'data': 0, 'error': 'not found'})
		art = Article.objects.filter(vuid=auid)
		data = ArticleSerializers(art).data
		return Response(data=data, status=status.HTTP_200_OK)

	def post(self, request, *args, **kwargs):
		""" 发表文章 """
		uuid = request.COOKIES['uuid']
		print('okok', request.data['title'], request.data['content'])
		user = MyUser.objects.filter(uuid=uuid)[0]
		art = Article()
		art.titile = request.data['title']
		art.user = user
		art.content = request.data['content']
		art.save()
		if not request.data:
			raise 'no'
		return Response({'data': 1})


class ImgList():
	pass


def login(request):
	return render(request, 'user/register.html')


def upload_img(request):
	return render(request, 'meterail/upload_image.html')


# def detail(request, type,  page):
# 	print(type,  page)
# 	return render(request, 'meterail/list.html')


ONE_PAGE_OF_DATA = 20


def get_posts(request, type_get):
	limit = 10
	type_get = int(type_get)
	page = request.GET.get('page')
	topics = ''
	if type_get == 1:
		topics = Image.objects.all()
	elif type_get == 2:
		topics = Video.objects.all()
	elif type_get == 3:
		topics = Article.objects.all()
	paginator = Paginator(topics, limit)

	try:
		topics = paginator.page(page)  # 获取某页对应的记录
	except PageNotAnInteger:  # 如果页码不是个整数
		topics = paginator.page(1)  # 取第一页的记录
	except EmptyPage:  # 如果页码太大，没有相应的记录
		topics = paginator.page(paginator.num_pages)  # 取最后一页的记录

	for i in topics:
		print(i.titile)

	return render(request, 'meterail/list.html', locals())


def detail(request, type_get):
	uid = request.GET.get('uid', '')
	print(type_get, uid)
	type_get = int(type_get)
	objs = ''
	if int(type_get) == 1:
		print('plplplp')
		objs = Image.objects.filter(iuid=uid)
	elif int(type_get) == 2:
		objs = Video.objects.filter(vuid=uid)
	elif int(type_get) == 3:
		objs = Article.objects.filter(vuid=uid)
	print(objs)
	return render(request, 'meterail/detail.html', locals())



def test(request):
	if request.method == 'POST':
		print(request.FILES.get('file'))
		from django.http import HttpResponse
		return HttpResponse('ok')