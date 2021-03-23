from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^', views.home, name='blog-home'),
    url(r'^about/', views.about, name='blog-about'),
]