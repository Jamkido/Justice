from django.db import models


class Contact(models.Model):
    f_name = models.CharField(max_length=100)
    s_name = models.CharField(max_length=111)
    email = models.EmailField()
    message = models.TextField()
    data_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.f_name
