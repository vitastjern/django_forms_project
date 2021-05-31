from django.contrib import admin

from .models import Contact, RegistredUser

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'text')

@admin.register(RegistredUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'email')

