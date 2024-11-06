from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["image"]


admin.site.register(UserProfile, UserAdmin)
