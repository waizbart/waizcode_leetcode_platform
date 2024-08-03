from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("home.urls")),
    path("assessment/", include("assessment.urls")),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls"))
]