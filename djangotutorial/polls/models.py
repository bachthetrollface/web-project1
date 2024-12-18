from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField("Question", max_length=200)
    date_posted = models.DateTimeField("Date posted")
