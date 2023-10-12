from django.contrib import admin
from django.urls import path
from home.views import *
from product.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeView, name="home"),
    path("home", homeView),
    path("index/1", homeView),
    path("product", product),
    path("addPage", addPage),
    path("productAdd", productAdd),
    path("delete", delete),
    path("register", register),
    path("login", login1)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
