from .models import MyUser
from django.contrib.auth.hashers import make_password, check_password
import datetime
from Pure import settings
import jwt


class UserServices(object):
	""" user model 操作 """
	@staticmethod
	def create_user(kwargs):
		''' 创建用户 '''
		user = MyUser(**kwargs)
		password = kwargs.pop('password')
		user.password = make_password(password)
		user.save()
		return user

	@staticmethod
	def check_user(mobile):
		user = MyUser.objects.filter(mobile=mobile)
		if user:
			return False
		else:
			return True

	@staticmethod
	def get_user(uuid):
		user = MyUser.objects.filter(uuid=uuid)
		if not user:
			return ''
		else:
			return user


def generate_jwt_data(user):
	"""
	:param user: 
	:return: jwt key
	"""
	expired_time = (datetime.datetime.now() +
					datetime.timedelta(hours=24))
	payload = {
		'uuid': user.uuid.hex,
		'exp': int(expired_time.timestamp()),
	}

	retdata = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256')
	return retdata.decode('utf-8'), expired_time


def get_client_ip(request):
	'''
	获取请求 ip
	:param object request
	:return str ip
	'''
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		return x_forwarded_for.split(',')[0]
	else:
		return request.META.get('REMOTE_ADDR', '127.0.0.1')