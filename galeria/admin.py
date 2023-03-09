from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id','nome','legenda', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )
    list_filter = ('categoria', )
    list_per_page = 10
    list_editable = ('publicada', )
    
admin.site.register(Fotografia, ListandoFotografias)    