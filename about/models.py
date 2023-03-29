from django.db import models
from django.contrib.auth.models import AbstractUser


# class Company(AbstractUser):


class Reason(models.Model):
    title = models.CharField(max_length=222)
    content = models.TextField()

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=222)
    answer = models.CharField(max_length=222)

    def __str__(self):
        return self.question
