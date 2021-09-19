from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import SnipeModel, User
# Register your models here.

admin.site.register(SnipeModel)
admin.site.register(User, UserAdmin)