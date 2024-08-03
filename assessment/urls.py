from django.urls import path

from . import views

urlpatterns = [
    # ex: /assessment/5
    path("<int:assessment_id>/", views.detail, name="detail"),
    # ex: /assessment/5/1
    path("<int:assessment_id>/<int:question_id>/", views.question, name="question"),
    # ex: /assessment/5/submit
    path("<int:assessment_id>/<int:question_id>/submit/", views.submit, name="submit"),
]