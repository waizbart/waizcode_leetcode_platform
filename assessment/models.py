from django.db import models

class Assessment(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    expected_output = models.CharField(max_length=200)
    input_text = models.CharField(max_length=200)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    def check_answer(self, answer):
        return self.expected_output == answer

class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    submission_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.submission_text