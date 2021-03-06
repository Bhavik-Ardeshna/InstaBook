from . import views
from django.urls import path

app_name = 'notification'

urlpatterns = [
    path('', views.ShowNotifications, name='show-notifications'),
    path('<noti_id>/delete', views.DeleteNotifications,
         name='delete-notification'),
]
