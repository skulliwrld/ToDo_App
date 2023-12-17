from django.db import models

# Create your models here.
class dolist(models.Model):
    title=models.CharField(max_length=10000)

    def __str__(self):
        return self.title
