import re
from datetime import datetime, timedelta
from rest_framework import serializers

from lg.settings import REGEX_MOBILE
from .models import VerifyCode
from django.contrib.auth import get_user_model

# 得到用户
User = get_user_model()


# 短信序列化器
class MSMSerializer(serializers.Serializer):
    # 手机号码
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码，是否注册，手机号是否合法，验证频率
        :param mobile:
        :return:
        """

        # 验证是否注册，如果不是0,显然已经存在--依赖数据库
        if User.objects.filter(mobile=mobile).count():
            #
            raise serializers.ValidationError("用户已经存在")

        # 验证手机号是否合法（是否正确手机号），如果不合法None,前面加上not 刚好满足进入if里面
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号不正确")

        # 验证短信发送频率（1分钟只能发送一次）--依赖数据库
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile).count():
            # 如果存在时间大于一分钟的，返回错误
            raise serializers.ValidationError("距离上次发送未超过60s")

        # 如果验证通过返回手机号码
        return mobile
