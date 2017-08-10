from django.contrib import admin
from django.contrib.auth.models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email_address', 'staff_status']
    list_display_links = ['id']
    list_editable = ['username']

admin.site.register(User, UserAdmin)