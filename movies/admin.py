from django.contrib import admin

# Register your models here.
from movies.models import movies

class m_display(admin.ModelAdmin):
    search_fields = ('Title',)
    list_display = ('Title','Genre')

admin.site.register(movies,m_display)
