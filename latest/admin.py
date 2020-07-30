from django.contrib import admin

from .models import Latest

class LatestAdmin(admin.ModelAdmin):
  list_display = ('id','title')
  
admin.site.register(Latest,LatestAdmin)