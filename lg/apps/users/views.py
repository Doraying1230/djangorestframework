from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend, get_user_model
from django.db.models import Q

User = get_user_model()


class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 根据用户名和电话查看用户
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            # 校验密码是否正确，正确就返回，否则不返回
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None

# # Create your views here.
# def index():
#     pass
