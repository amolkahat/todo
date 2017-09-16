from django.db import models

# Create your models here.

class tasks(models.Model):
    task_text = models.CharField(max_length=500)
    added_date = models.DateTimeField('added date')
    completed_date = models.DateTimeField('completed date', blank=True)
    state = models.IntegerField(default=-1)

    def __str__(self):
        return self.task_text
