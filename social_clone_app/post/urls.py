from django.urls import path
from . import views

app_name = 'post'


urlpatterns = [
    path('', views.Index, name='index'),
    path('newpost/', views.NewPost, name='newpost'),
    path('<uuid:post_id>', views.PostDetails, name="postdetails")
]
