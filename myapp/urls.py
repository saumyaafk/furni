
from django.urls import path
from .views import index,about,blog

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('blog/',blog,name='blog'),
]
