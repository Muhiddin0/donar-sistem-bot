from django.contrib import admin
from .models import TempUser, User

# Register your models here.
admin.site.register(TempUser)
admin.site.register(User)
