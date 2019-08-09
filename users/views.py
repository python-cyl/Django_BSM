from django.shortcuts import render
from django.views.generic.base import View
from users.models import UserProfile
from django.contrib.auth import authenticate, login

# Create your views here.

class UserView(View):
    def get(self, request):
        return render(request, 'Empt classroom.html', {})
    def post(self, request):
        user_name = request.POST.get("username", "")
        user_password = request.POST.get("password", "")
        try:
            user_test = UserProfile.objects.get(username=user_name)
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                login(request, user)
                return render(request, 'Empt classroom.html', {})
            else:
                return render(request, 'log.html', {"msg": '用户名或密码错误'})
        except UserProfile.DoesNotExist:
            return render(request, 'log.html', {"msg": '登陆信息错误'})

