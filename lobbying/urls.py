from django.conf.urls import url

from lobbying import views

urlpatterns = [
    url(r'^(?P<id>\w+)', views.search, name='search'),
    url(r'^$', views.Index, name='index'),
]