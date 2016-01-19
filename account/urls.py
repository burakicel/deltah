from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout',name='logout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^offer/$', views.offer, name='offer'),
    url(r'^transaction/$', views.transaction, name='transaction'),
    url(r'^deals/$', views.deals, name='deals'),
    url(r'^rewards/$', views.rewards, name='rewards'),
    url(r'^history/$', views.history, name='history'),
    url(r'^$', views.dashboard, name='dashboard'),
]