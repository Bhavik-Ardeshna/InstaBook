from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from notifications.models import Notification


@login_required
def ShowNotifications(request):
    user = request.user
    notification = Notification.objects.filter(user=user).order_by("-date")
    Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)

    context = {
        'notifications': notification,
    }
    return render(request, "notifications.html", context)


def DeleteNotifications(request, noti_id):
    user = request.user
    Notification.objects.filter(id=noti_id, user=user).delete()
    return redirect('notification:show-notifications')


def CountNotifications(request):
    count_notification = 0
    if request.user.is_authenticated:
        count_notification = Notification.objects.filter(
            user=request.user, is_seen=False).count()

    return {'count_notifications': count_notification}
