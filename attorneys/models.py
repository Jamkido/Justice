from django.db import models


class Attorneys(models.Model):
    name = models.CharField(max_length=222)
    image = models.ImageField(upload_to='media/images')
    occupation = models.CharField(max_length=222)
    content = models.TextField()

    class Meta:
        verbose_name = 'Attorney'
        verbose_name_plural = 'Attorneys'

    def __str__(self):
        return self.name


class Happy_Clients(models.Model):
    name = models.CharField(max_length=222)
    job = models.CharField(max_length=222)
    comment = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Happy_Client'
        verbose_name_plural = 'Happy_Clients'
