"""lg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
import xadmin
from lg.settings import MEDIA_ROOT
from django.views.static import serve
from goods.views import GoodsListViewSet, CategoryViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from users.views import SMSCodeViewSet, UserRegViewset

# 实例化默认路由
router = DefaultRouter()

# 注册商品列表
router.register(r'goods', GoodsListViewSet)
# 注册商品类别
router.register(r'category', CategoryViewSet)
# 短信注册
router.register(r'codes', SMSCodeViewSet, base_name="codes")
# 用户手机注册,要加上base_name否则报错
router.register(r'register', UserRegViewset, base_name="register")
# 这种配置很方便，后面就会体现出来
goods_list = GoodsListViewSet.as_view({
    # get请求绑定ListModelMixin的list方法
    'get': 'list',
})

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^goods/$', goods_list, name="goods_list"),
    url(r'^ueditor/', include('DjangoUeditor.urls')),

    url(r'^', include(router.urls)),

    # 支持文档生成的url,结尾一定不能写$
    url(r'docs/', include_docs_urls(title="***商店")),
    # 登录时候用的url,调试api的时候用到
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # token认证
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的认证,修改一个名字
    url(r'^login/', obtain_jwt_token),

]
