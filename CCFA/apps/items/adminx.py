import xadmin
from .models import ProjectInfo,ImageInfo


class ProjectInfoXadmin(object):
    list_display = ["title", "desc", "love_num", "image", "nums", "status", "category", "money_total", "money_ing",
                    "projectInfo", "days", "is_status"]
    search_fields = ["title", "desc", "love_num", "image", "nums", "status", "category", "money_total", "money_ing",
                     "projectInfo", "days", "is_status"]
    list_filter = ["title", "desc", "love_num", "image", "nums", "status", "category", "money_total", "money_ing",
                   "projectInfo", "days", "is_status"]
    style_fields = {"image": "ueditor"}


class ImageInfoXadmin(object):
    list_display=[""]



xadmin.site.register(ProjectInfo, ProjectInfoXadmin)
