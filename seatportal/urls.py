from django.conf.urls import url

from seatportal import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'vacant/', views.vacant),
    url(r'republican/', views.republican),
    url(r'democrat/', views.democrat),
    url(r'cl1/', views.class1),
    url(r'cl2/', views.class2),
    url(r'cl3/', views.class3),
]