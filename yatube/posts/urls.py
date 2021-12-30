from django.urls import path
#from django.urls.resolvers import URLPattern
from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'main'),
    path('group/<slug:slug>/', views.group_posts, name = 'group_posts'),
]

