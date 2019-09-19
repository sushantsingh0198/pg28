from django.db import models


# Create your models here.
class TeacherDetail(models.Model):
    name = models.CharField(max_length=128)
    e_code = models.CharField(max_length=6)
    available_load = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name} {self.e_code}'


class ClassDetail(models.Model):
    sem = models.CharField(max_length=32)
    cls = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.sem} {self.cls}'
