from django.urls import path

from . import views

urlpatterns = [
    # ex: /assessment
    path("", views.index, name="index"),
    # ex: /assessment/5
    path("<int:assessment_id>/", views.detail, name="detail"),
    # ex: /assessment/5/results
    path("<int:assessment_id>/results/", views.result, name="result"),
    # ex: /assessment/5/1
    path("<int:assessment_id>/<int:question_id>/", views.question, name="question")
]