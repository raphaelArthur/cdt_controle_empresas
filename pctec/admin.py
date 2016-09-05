from django.contrib import admin

from .models import Empresa, Colaborador

admin.site.register(Empresa)
admin.site.register(Colaborador)
fields = ( 'image_tag', )
readonly_fields = ('image_tag',)
