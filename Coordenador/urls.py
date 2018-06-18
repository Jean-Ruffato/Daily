from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^coordenador/cadastrar-usuario$', views.signup, name='cadastrar_usuario'),
    url(r'^coordenador/definir-atividade$', views.definir_atividade, name='definir_atividade'),
    url(r'^coordenador/$', views.home, name='home'),
    url(r'^coordenador/usuarios$', views.usuarios, name='usuarios'),
    url(r'^coordenador/cadastrar-projeto$', views.cadastrar_projeto, name='cadastrar_projeto'),
    url(r'^coordenador/perfil_projeto/(?P<pk>\d+)/$', views.perfil_projeto, name='perfil_projeto'),
    url(r'^coordenador/perfil_projetos/$', views.perfil_projetos, name='perfil_projetos'),
    url(r'^coordenador/apagar_projeto/(?P<pk>\d+)', views.apagar_projeto, name='apagar_projeto'),
    url(r'^coordenador/editar_projeto/(?P<pk>\d+)/$', views.editar_projeto, name='editar_projeto'),
    url(r'^coordenador/editar_usuarios/(?P<pk>\d+)/$', views.editar_usuarios, name='editar_usuarios'),
    url(r'^coordenador/editar_atividade/(?P<pk>\d+)/$', views.editar_atividade, name='editar_atividade'),
    url(r'^coordenador/integrantes/(?P<pk>\d+)/$', views.integrantes, name='integrantes')
]
