from django.contrib import admin

from .models import Newscontent

class NewscontentAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'published_date',)
  list_display_links = ('title',)
  list_filter =(('published_date'),)
admin.site.register(Newscontent,NewscontentAdmin)
