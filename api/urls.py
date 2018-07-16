from sys import path

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from Funcionarios.views import ProjetosListView, ProjetosIDView, AtividadesListView, AtividadesIDView, PerfilListView

urlpatterns = [
    url(r'^api/projetos/$', ProjetosListView.as_view(), name='projetos_list'),
    url(r'^api/atividades/$', AtividadesListView.as_view(), name='atividades'),
    url(r'^api/perfis/$', PerfilListView.as_view(), name='perfis'),
    url(r'^api/projetos/(?P<pk>[0-9]+)/$', ProjetosIDView.as_view(), name='projetos_id'),
    url(r'^api/atividades/(?P<pk>[0-9]+)/$', AtividadesIDView.as_view(), name='atividades_id'),
    url('login/', obtain_jwt_token),
    url('refresh-token/', refresh_jwt_token),
]
