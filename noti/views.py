from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic.base import View
from django.urls import reverse
from .models import Noti
import json
import datetime
from notifications.signals import notify
from notifications.models import Notification
from users.models import UserProfile
from django.core import serializers


# Create your views here.

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

class NotiView(View):

    def delete_my_read_notifications(request):
        notifications = request.user.notifications.read()
        notifications.delete()
        return render(request, 'my_notifications.html')

    def my_notifications(my_notification_pk):
        my_notification = get_object_or_404(Noti, pk=my_notification_pk)
        my_notification.unread = False
        my_notification.save()

    def get(self, request):
        re = request.user.notifications.all().values('pk', 'recipient', 'actor_content_type', 'verb', 'description')
        # actor_content_type == 7 为站内消息   3 为组内消息
        time = request.user.notifications.all().values('timestamp')
        new_time = json.dumps(list(time), cls=ComplexEncoder)
        # rr = serializers.serialize('json', re)
        rr = json.dumps(list(re))
        return HttpResponse(rr+new_time)


    def get_user_notification(request):
        re = request.user.notifications.all().values('recipient', 'description', 'timestamp')
        rr = json.dumps(re)


    def send_notification(request):
        actor = request.user
        type = Notification.objects
        user1 = UserProfile.objects.get(id=3)
        user2 = UserProfile.objects.get(id=5)
        # user3 = UserProfile.objects.filter(is_active=1)
        notify.send(actor, recipient=[user1, user2], verb='you reached level 10')
        return HttpResponse("ok")
    #     return render(request, 'notifications_form.html')
    # actor = request.user
#         # content = request.POST.get("content", "")
#         # recipient = request.POST.get("id", "")
#         # noti = Noti()
#         # noti.content = content
#         # noti.receiver = recipient
#         # noti.sender = actor
#         #
#         #
#         # verb = "{0}给你发来一条消息".format(actor)
#         # real = Noti.objects.get(receiver=recipient)
#         # comment = "发送成功"
#         # try:
#         #     if real is not None:
#         #         notify.send(actor, recipient=recipient, verb=verb, action_object=content)
#         #         return render(request, 'notifications_form.html', comment)
#         # except Noti.DoesNotExist():
#         #     return render(request, 'notifications_form.html', '发送失败')
