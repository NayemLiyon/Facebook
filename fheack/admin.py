from django.contrib import admin
from .models import FacebookLogin

# Register your models here.
class FacebookAdmin(admin.ModelAdmin):
    list_display = ['emailNum','password']
    search_fields = ['emailNum']

admin.site.register(FacebookLogin,FacebookAdmin)