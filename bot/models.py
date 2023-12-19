from django.db import models


class User(models.Model):
    user_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.first_name)