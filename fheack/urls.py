#my import
from django.urls import path
from . import views
from .views import Album_Create



app_name='fheack'
urlpatterns = [
     path('', views.Album_Create.as_view(),name='create'),
    path('create/', views.index,name='index'),
]
