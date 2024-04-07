from django.contrib import admin

from .models import Question, Submission, Assessment

admin.site.register(Assessment)
admin.site.register(Question)
admin.site.register(Submission)