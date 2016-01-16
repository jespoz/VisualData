from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'apps.users.views.userlogin', name="login"),
	url(r'^register/$', 'apps.users.views.userregister', name="register"),
)