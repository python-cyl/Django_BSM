from django.contrib import admin

# Register your models here.
from .models import Noti

class NotiAdmin(admin.ModelAdmin):
    pass

admin.site.register(Noti, NotiAdmin)