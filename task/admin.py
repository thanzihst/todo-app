from django.contrib import admin

# Register your models here.

from  task.models import User


admin.site.register(User)