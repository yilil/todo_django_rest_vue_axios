from django.db import models
import datetime
from . import validators


class Task(models.Model):
    TODO = 'Todo'
    DONE = 'Done'

    STATUS_CHOICES = (
        (TODO, 'Todo'),
        (DONE, 'Done')
    )

    description = models.CharField(max_length=255, validators=[validators.descriptionValidator])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)
    due = models.DateField(default=datetime.date.today() + datetime.timedelta(days=7),
                           validators=[validators.dateValidator])
