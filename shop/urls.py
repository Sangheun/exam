from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.category_detail, name='category_detail'),
    url(r'^(?P<post_pk>\d+)/category/new/$', views.category_new, name='category_new'),

]