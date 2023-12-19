from django.db import models


# Create your models here.
class TempUser(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    region = models.PositiveIntegerField()
    organizations = models.PositiveIntegerField()
    position = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    reject = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    region = models.PositiveIntegerField()
    organizations = models.PositiveIntegerField()
    position = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.name
        