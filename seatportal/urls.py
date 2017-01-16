from django.conf.urls import url

from seatportal import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'vacant/', views.vacant),
    url(r'republican/', views.republican),
    url(r'democrat/', views.democrat)
]