from . import views
from django.urls import path

app_name = 'account'

urlpatterns = [
    path('', views.LoginView, name='login'),
    path('signup/', views.SignView, name='signup'),
    path('logout/', views.SignOutView, name='signout'),

]
