from django.contrib import admin
from .models import (
    User
)


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'middle_name', 'phone']


admin.site.register(User, UserAdmin)
