from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^multincubadora/$', views.multi_princ, name='multi_princ'),
    url(r'^multincubadora/cracha/(?P<colaborador_id>[0-9]+)/$', views.cracha, name='cracha'),
    url(r'^multincubadora/graduadas/$', views.graduadas, name='graduadas'),

    url(r'^multincubadora/incubadas/$', views.incubadas, name='incubadas'),
    url(r'^multincubadora/incubadas/(?P<incubada_id>[0-9]+)/$', views.empresas_detalhe, name='empresas_detalhe'),
    url(r'^multincubadora/incubadas/(?P<incubada_id>[0-9]+)/(?P<colaborador_id>[0-9]+)/$', views.colaborador, name='colaborador'),


    url(r'^multincubadora/projr/$', views.projr, name='projr'),
    url(r'^multincubadora/projr/(?P<jr_id>[0-9]+)/$', views.projr_detalhe, name='projr_detalhe'),

    url(r'^multincubadora/atendimento/$', views.atendimento, name='atendimento'),

    url(r'^multincubadora/consultores/$', views.consultores, name='consultores'),

    url(r'^multincubadora/profs_labs/$', views.profs_labs, name='profs_labs'),

]    