from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^exportar_atividades/$', views.exportar_atividades, name='exportar_atividades'),
    url(r'^exportar_projetos/$', views.exportar_projetos, name='exportar_projetos'),
    url(r'^exportar_usuarios/$', views.exportar_usuarios, name='exportar_usuarios')
]
