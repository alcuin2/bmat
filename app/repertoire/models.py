from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class File(models.Model):

    id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=255)
    work_count = models.IntegerField()


class Work(models.Model):

    id = models.AutoField(primary_key=True)
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='works')
    proprietary_id = models.IntegerField()
    iswc = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    contributors = ArrayField(models.CharField(max_length=255))

