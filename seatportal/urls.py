from django.conf.urls import url

from seatportal import views

urlpatterns = [
    url(r'^$', views.index),
]