from django.db import models

# Create your models here.

class Noti(models.Model):
    publish_data = models.DateTimeField(verbose_name=u"发布日期")
    content = models.CharField(max_length=500, verbose_name=u"内容")
    title = models.CharField(max_length=100, verbose_name=u"标题")
    type = models.CharField(max_length=1, verbose_name=u"消息类型", choices=(('0', "全站消息"), ('1', "组内消息"), ('2', "个人消息")), default="2")
    receiver = models.CharField(max_length=100, verbose_name=u"接收者")
    sender = models.CharField(max_length=1, verbose_name=u"发布者", choices=(('0', "管理员"), ('1', "副组长"), ('2', "系统")))

    class Meta:
        verbose_name = u"站内消息"
        verbose_name_plural = verbose_name
