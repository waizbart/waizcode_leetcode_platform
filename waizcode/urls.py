from django.urls import path

from . import views

urlpatterns = [
    # ex: /waizcode/
    path("", views.index, name="index"),
    # ex: /waizcode/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /waizcode/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
]