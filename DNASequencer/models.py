from datetime import datetime

from django.db import models


# Create your models here.
from django.utils import timezone





class SearchRequest(models.Model):
    inputSequence = models.CharField(max_length=200)
    created_by = models.IntegerField()
    created_on = models.DateTimeField(default=timezone.now())
    update_on = models.DateTimeField(default=timezone.now())


class Task(models.Model):
    TASK_STATUS_CHOICES = [
        (1, 'Created'),
        (2, 'Processing'),
        (3, 'Success'),
        (4, 'Failed'),
    ]

    input_id = models.ForeignKey(SearchRequest, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=TASK_STATUS_CHOICES, default=1)

    created_on = models.DateTimeField(default=timezone.now())
    update_on = models.DateTimeField(default=timezone.now())


class Result(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    protein_name = models.CharField(max_length=200)
    sequence_location = models.CharField(max_length=200)

    created_on = models.DateTimeField()
