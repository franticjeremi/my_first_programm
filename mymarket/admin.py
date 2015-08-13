from django.contrib import admin

# Register your models here.
from .models import Mymarket, Configuration

class ConfigurationInline(admin.StackedInline):
    model = Configuration
    extra = 1

class MymarketAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'url']
    inlines = [ConfigurationInline]
    list_display = ('name', 'url')
    
admin.site.register(Mymarket, MymarketAdmin)