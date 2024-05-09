from django.contrib import admin
from .models import beurlaubung

class BeurlaubungAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'klasse', 'datum_gestellt', 'tutor', 'begruendung']  # Zeige diese Felder in der Listenansicht an
    search_fields = ['name', 'klasse', 'tutor']  # Aktiviere die Suche nach diesen Feldern

admin.site.register(beurlaubung, BeurlaubungAdmin)

