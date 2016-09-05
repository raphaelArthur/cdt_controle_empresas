from django.contrib import admin

from .models import Incubada, Graduada, Empresa_Junior, Automovel, Colaborador_multi, Consultores, Colaborador_Empresa_Junior

admin.site.register(Incubada)
admin.site.register(Graduada)
admin.site.register(Empresa_Junior)
admin.site.register(Automovel)
admin.site.register(Colaborador_multi)
admin.site.register(Colaborador_Empresa_Junior)
admin.site.register(Consultores)
fields = ( 'image_tag', )
readonly_fields = ('image_tag',)

