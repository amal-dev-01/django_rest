from django.db import models

# Create your models here.


class Students(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    distict = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    