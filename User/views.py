# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from django.db import transaction
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from .services import UserServices, generate_jwt_data, get_client_ip
from django.contrib import auth
import datetime
from Pure import settings
from .models import MyUser
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


class UserRegister(APIView):
	""" 用户注册"""
	@transaction.atomic
	def post(self, request, *args, **kwargs):
		if UserServices.check_user(request.data['mobile']):
			serializer = UserRegisterSerializer(data=request.data)
			serializer.is_valid(raise_exception=True)
			valid_data = serializer.validated_data
			user = UserServices.create_user(valid_data)
			return Response({'detail': 'ok', 'uuid': user.uuid}, status=status.HTTP_200_OK)
		else:
			return Response({'detail': '用户已存在', 'data': 1})


class UserLogin(APIView):
	""" 用户登录 """
	@transaction.atomic
	@csrf_exempt
	def post(self, request, *args, **kwargs):
		mobile, password = request.data.get('mobile'), request.data.get('password')
		user = auth.authenticate(username=mobile, password=password)
		if not user:
			return Response({'登录失败', 1})
		response = Response({'detail': 'ok'}, status=status.HTTP_200_OK)
		try:
			jwtcode, expired_time = generate_jwt_data(user)
			expired_time = datetime.datetime.strftime(expired_time,
													  '%a, %d-%b-%Y %H:%M:%S GMT')
			max_age = settings.AUTH_EXPIRED_HOURS * 3600
			cache_key = 'user_{}'.format(user.uuid.hex)
			cache.set(cache_key, user, 2 * 3600)
			response.set_cookie('_puremach',
								jwtcode,
								max_age=max_age,
								expires=expired_time,
								)
			response.set_cookie('uuid',
								user.uuid)
		except:
			response.data = {'detail': 'jwt 信息生成异常'}
			response.status_code = 400

		user.login_ip = get_client_ip(request)
		user.last_login = datetime.datetime.now()
		user.save()

		return response


class UserInfo(APIView):
	""" 获取用户的详细信息"""

	@transaction.atomic
	def post(self, request):
		uuid = request.data.get('uuid')
		user = UserServices.get_user(uuid)
		if user:
			return Response({'mobile': user[0].mobile, 'name': user[0].nick})
		return Response({'detail': '搜索不到用户信息'})


def index(request):
	return render(request, 'user/profile.html')


def profile(request):
	uuid = request.GET.get('uuid')
	if uuid:
		user = MyUser.objects.filter(uuid=uuid)
	return render(request, 'user/userinfo.html', locals())