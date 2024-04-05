from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("waizcode/", include("waizcode.urls")),
    path("admin/", admin.site.urls),
]