from django.conf.urls import url

from polling import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^test', views.seatview),
    url(r'^seat/(?P<state>\w+)/$', views.seatview),
]