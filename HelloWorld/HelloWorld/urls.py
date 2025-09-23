"""
URL configuration for HelloWorld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
from . import views, testdb, search, search2, TikTokApi

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", views.hello, name="hello"),
    path("runoob/", views.runoob, name="runoob"),
    path("extendTpl/", views.extendTpl, name="extendTpl"),
    path("upload/", views.uploadFile, name="upload"),
    path("uploadView/", views.uploadView, name="uploadView"),
    # ticktok模拟数据API
    path("api/v1/container/scan_ip/", TikTokApi.scan_ip, name="scan_ip"),
    path("api/v1/container/check_index/", TikTokApi.check_index, name="check_index"),
    path("api/v1/process/", TikTokApi.myProcess, name="myProcess"),
    path("saveDB/", testdb.saveDB),
    path("queryDB/", testdb.queryDB),
    path("updateDB/", testdb.updateDB),
    path("deleteDB/", testdb.deleteDB),
    path("search-form/", search.search_form, name="search-form"),
    path("search/", search.search, name="search"),
    re_path(r"^search-post/$", search2.search_post, name="search-post"),
]
