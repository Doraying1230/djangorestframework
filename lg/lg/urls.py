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
# from django.views.generic import TemplateView

import xadmin
from lg.settings import MEDIA_ROOT
from django.views.static import serve

from goods.views_base import GoodsListView
# from rest_framework.documentation import include_docs_urls
from rest_framework.documentation import include_docs_urls

# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^goods/$', GoodsListView.as_view(), name="goods_list"),

    # 支持文档生成的url,结尾一定不能写$
    url(r'docs/', include_docs_urls(title="***商店")),
    # 登录时候用的url,调试api的时候用到
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^index/', TemplateView.as_view(template_name='index.html'), name="index"),

]
