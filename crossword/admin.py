from django.contrib import admin

from .models import Crossword, Crosswordcheck

class CrosswordAdmin(admin.ModelAdmin):
  list_display = ('id','word','clue')
admin.site.register(Crossword,CrosswordAdmin)

class CrosswordcheckAdmin(admin.ModelAdmin):
  list_display = ('id','result','email','subscribe_yes')
admin.site.register(Crosswordcheck,CrosswordcheckAdmin)