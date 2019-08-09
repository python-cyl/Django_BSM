# !/usr/bin/env/ python
# _*_ coding:utf-8 _*_
from notifications.signals import notify
from django.contrib.auth.models import User
from .models import Noti
from django.db.models.signals import post_save
from django.dispatch import receiver


# @receiver(post_save, sender=Noti)
def send_notification(request):
    # # 信息发布者
    actor = request.user
    # # 信息接收者
    # # reciver = request.POST.get()
    # # recipient = Noti.objects.get(receiver=receiver)
    # recipient = request.user
    # # 动作
    # verb = '{0}给你发来一条消息'.format(actor)
    # # 消息
    # content = Noti.content
    #
    # notify.send(actor, recipient=recipient, verb=verb, action_object=content)

    user1 = User.objects.get(id = 4)
    user2 = User.objects.get(id = 5)
    notify.send(actor, recipient=[user1, user2], verb='you reached level 10')