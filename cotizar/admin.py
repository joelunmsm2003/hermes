from django.contrib import admin
from cotizar.models import *
from django.contrib.admin.filters import RelatedOnlyFieldListFilter


@admin.register(Anio)
class AnioAdmin(admin.ModelAdmin):
    list_display = ('id_anio','anio_antig')

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id_marca','name_marca')





# Some SimpleListFilter filters
@admin.register(AutoValor)
class AutoValorAdmin(admin.ModelAdmin):


	list_display = ('get_marca','get_modelo','traccion')
	list_filter = (
		('id_marca', RelatedOnlyFieldListFilter),
	)
	admin_order_field = ('id_marca',)

	def get_marca(self, obj):
		return obj.id_marca.name_marca
	get_marca.short_description = 'Marca'
	get_marca.admin_order_field = 'autovalor__id_marca'

	def get_modelo(self, obj):
		return obj.id_modelo.name_model
	get_modelo.short_description = 'Modelo'
	get_modelo.admin_order_field = 'autovalor__id_modelo'





# @admin.register(AutoValor)
# class AutoValorAdmin(admin.ModelAdmin):
	
# 	list_display = ('get_marca','get_modelo','traccion')
	
# 	def get_marca(self, obj):
# 		return obj.id_marca.name_marca
# 	get_marca.short_description = 'Marca'
# 	get_marca.admin_order_field = 'autovalor__id_marca'

# 	def get_modelo(self, obj):
# 		return obj.id_modelo.name_model
# 	get_modelo.short_description = 'Modelo'
# 	get_modelo.admin_order_field = 'autovalor__id_modelo'
