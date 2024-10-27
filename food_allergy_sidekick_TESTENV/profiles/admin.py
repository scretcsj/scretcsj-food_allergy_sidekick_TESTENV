from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'display_allergies']

    def display_allergies(self, obj):
        return ", ".join(obj.allergies)  # Directly access the MSFList
    display_allergies.short_description = 'Allergies'

admin.site.register(UserProfile, UserProfileAdmin)
