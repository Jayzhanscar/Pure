from django.conf.urls import url, re_path, include

from User import views
urlpatterns = [
	re_path(r'^index$', view=views.index, name="home"),
	re_path(r'^register$', views.UserRegister.as_view(), name="register"),
	re_path(r'^login$', views.UserLogin.as_view(), name="login"),
	re_path(r'^userinfo$', views.UserInfo.as_view(), name="userinfo"),
	re_path(r'^profile$', view=views.profile)
]