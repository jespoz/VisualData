from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^dashboard/$', 'apps.dashboard.views.dashboard', name="dashboard"),
)