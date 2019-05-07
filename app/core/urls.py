
from django.urls import path
from . import views

urlpatterns = [
    path('get_mongo/', views.get_mongo, name='get_mongo'),
    path('get_rabbit/', views.get_rabbit, name='get_rabbit')
]
