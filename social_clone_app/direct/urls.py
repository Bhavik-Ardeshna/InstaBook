from django.urls import path
from direct.views import Inbox

app_name = 'direct'


urlpatterns = [
    path('', Inbox, name='inbox'),
]
