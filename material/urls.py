from django.conf.urls import url, re_path, include

from material import views
urlpatterns = [
	re_path(r'api/img$', view=views.ImgGet.as_view(), name="api"),
	re_path(r'api/video$', view=views.VideoGet.as_view(), name="video"),
	re_path(r'api/article$', view=views.ArticleGet.as_view(), name="article"),
	re_path(r'login$', view=views.login, name="login"),
	re_path(r'upload$', view=views.upload_img, name="upload"),
	re_path(r'test$', view=views.test, name="test"),
	url(r'detail/(?P<type_get>\w+)$', view=views.get_posts, name='detail'),
	url(r'list/(?P<type_get>\w+)$', view=views.detail, name='list')
]