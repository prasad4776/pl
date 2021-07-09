from django.db import models


# Create your models here.


class Plays(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    contact_no = models.IntegerField()

    def __str__(self):
        return self.name
