from django.db import models


class Works(models.Model):
    title = models.CharField(max_length=222)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return self.title
