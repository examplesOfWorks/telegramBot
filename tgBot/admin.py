from django.contrib import admin

from .forms import ProfileForm
from .models import Profile
from .models import Message

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name')
    form = ProfileForm

@admin.register(Message)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'created_at')
