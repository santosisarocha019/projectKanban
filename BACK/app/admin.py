from django.contrib import admin
from .models import *

class detUsuario(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Usuario, detUsuario)

class detTarefa(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'nome_setor', 'prioridade', 'data_cadastro')
    list_display_links = ('id', 'descricao',)
    search_fields = ('descricao',)
    list_per_page = 10

admin.site.register(Tarefa, detTarefa)

# Register your models here.
