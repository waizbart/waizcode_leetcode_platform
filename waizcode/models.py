from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    expected_output = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    submission_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.submission_text