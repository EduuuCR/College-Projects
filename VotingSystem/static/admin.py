from django.contrib import admin
from .models import Competition, Entry

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ('name', 'description')
    list_filter = ('start_date', 'end_date')

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'competition', 'user', 'votes')
    search_fields = ('title', 'description')
    list_filter = ('competition',)
