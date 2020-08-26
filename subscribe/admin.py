from django.contrib import admin

from .models import Subscribe

class SubscribeAdmin(admin.ModelAdmin):
  list_display = ('id', 'email', 'contact_date')
  list_display_links = ('id', 'email')

admin.site.register(Subscribe, SubscribeAdmin)