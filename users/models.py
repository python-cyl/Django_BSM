from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
   student_number = models.CharField(max_length=10, verbose_name=u"学号", default='')
   student_name = models.CharField(max_length=10, verbose_name=u"姓名", default='')
   student_password = models.CharField(max_length=6, verbose_name=u"密码", default='')

   class Meta:
       verbose_name = "登陆信息"
       verbose_name_plural = verbose_name

   def __str__(self):
       return self.username
