from django.db import models
import datetime
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='./polls/archive/polls/')
status = ['Новый', 'исправлено', 'прочее']


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')
    file = models.FileField(max_length=100, default='DEFAULT VALUE', storage=fs)

    class Meta:
        verbose_name = u"Создать запись"
        verbose_name_plural = u"Создать Запись"

    def loaded_file(self, filename):
        return 'Question_{0}/{1}'.format(self.file.id, filename)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    file = models.FileField(max_length=100, default='DEFAULT VALUE', storage=fs)

    def loaded_file(self, filename):
        return 'Question_{0}/{1}'.format(self.file.id, filename)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = u"Просмотр и оценка объекта"
        verbose_name_plural = u"Просмотр и оценка объектов"
