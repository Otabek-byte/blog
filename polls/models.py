from django.db import models
import datetime
from django.utils import timezone
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='./polls/archive/polls/')
status = ['Новый', 'исправлено', 'прочее']

# Create your models here.

class Question(models.Model):
    file = models.FileField(max_length=100, default='DEFAULT VALUE', storage=fs)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    def loaded_file(instance, filename):
        return 'Question_{0}/{1}'.format(instance.file.id, filename)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Object(models.Model):
    dwg = models.FileField(max_length=250, default='', storage=fs)
    dwg_text = models.CharField(max_length=500)
    dwg_time = models.DateTimeField(auto_now=False)
    dwg_choice = models.TextChoices()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
