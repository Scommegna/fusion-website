from django.contrib import admin

from .models import Cargo, Servicos, Funcionario

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'active', 'modified',)
    
@admin.register(Servicos)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('service', 'icon', 'active', 'modified')
    

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'cargo', 'active', 'modified')