from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pctec/$', views.pctec, name='pctec'),
    url(r'^pctec/(?P<empresa_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^pctec/(?P<empresa_id>[0-9]+)/(?P<colaborador_id>[0-9]+)/$', views.colaborador, name='colaborador'),
    url(r'^pctec/cracha/(?P<colaborador_id>[0-9]+)/$', views.cracha, name='cracha'),
]