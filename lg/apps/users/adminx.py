from xadmin import views
import xadmin
from .models import VerifyCode


class GlobalSettings(object):
    # 网站标题
    site_title = "***商店后台"
    # 网站页面的起始目录
    site_footer = "myself 289237642"


class VerifyCodeAdmin(object):
    # 字段控制显示
    list_display = ['code', 'mobile', "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
