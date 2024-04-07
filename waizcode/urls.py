from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("assessment/", include("assessment.urls")),
    path("admin/", admin.site.urls),
]