from django.urls import path
from . import views

app_name = '<url_shorten'  # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('shortened', views.shortened, name='short')
]
