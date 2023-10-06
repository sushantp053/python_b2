from django.contrib import admin
from django.urls import path
from home.views import *
from product.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeView, name="home"),
    path("home", homeView),
    path("index/1", homeView),
    path("product", product),
    path("addPage", addPage),
    path("productAdd", productAdd),
]
