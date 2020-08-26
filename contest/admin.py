from django.contrib import admin

from .models import Storytitle

class StorytitleAdmin(admin.ModelAdmin):
  list_display = ('id','title','name','email')
admin.site.register(Storytitle,StorytitleAdmin)