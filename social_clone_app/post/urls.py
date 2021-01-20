from django.urls import path
from . import views

app_name = 'post'


urlpatterns = [
    path('',views.Index,name='index'),
    path('newpost/',views.NewPost,name='newpost'),

]