from django.contrib.auth.backends import ModelBackend, get_user_model
from django.db.models import Q
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from users.models import VerifyCode
from users.serializers import MSMSerializer, UserRegSerializer
from utils.yunpian import YunPian
import random

# 得到当前用户实例对象
User = get_user_model()


# 用户使用短信注册
class UserRegViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    # 用户
    queryset = User.objects.all()
    # 配置注册序列化器
    serializer_class = UserRegSerializer


class CustomModelBackend(ModelBackend):

    # 方法的的username是一个参数：传入账号和手机号
    def authenticate(self, request, username=None, password=None, **kwargs):
        print("username==", username)
        print("password==", password)
        print("request===", request)

        try:
            # 根据手机号和用户名查找用户
            user = User.objects.get(Q(username=username) | Q(mobile=username))
            # 校验密码是否正确
            if user.check_password(password):
                return user


        except Exception as e:
            print(e)
            return None


# 发送验证码并且保存验证码
# CreateModelMixin,post请求，保存验证码
class SMSCodeViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = VerifyCode.objects.all()

    # 配置序列化器
    serializer_class = MSMSerializer

    # 生成验证码
    def get_code(self):
        """得到验证码,长度4"""
        data = "0123456789"
        # 列表
        reuslt = []  # 1,2,5,7,
        for i in range(4):
            reuslt.append(random.choice(data))

        return "".join(reuslt)

    # 当保存数据的时候调用
    def create(self, request, *args, **kwargs):
        # 得到序列化器
        serializer = self.get_serializer(data=request.data)

        # 执行序列化器里面的校验功能
        serializer.is_valid(raise_exception=True)

        # 保存数据到数据库，自定义生成验证码后，在使用
        # self.perform_create(serializer)

        # 取到电话号码
        mobile = serializer.data["mobile"]

        # 验证码
        code = self.get_code()

        yp = YunPian()
        # 发送验证码
        response_data = yp.set_msg(mobile, code)

        if response_data["code"] == 0:
            # 发送验证码成功

            # 保存验证码和收好到数据库里面
            VerifyCode(mobile=mobile, code=code).save()  # 保存手机号码和验证码

            return Response({"mobile": mobile, "msg": response_data["msg"]}, status=status.HTTP_201_CREATED)

        else:
            # "发送验证码失败"
            return Response({"mobile": mobile, "msg": response_data["msg"]}, status=status.HTTP_400_BAD_REQUEST)
