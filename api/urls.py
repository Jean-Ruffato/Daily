from django.conf.urls import url
from Funcionarios.views import ProjetosView, AtividadesView, PerfilView

urlpatterns = [
    url(r'^api/projetos/$', ProjetosView.as_view(), name='projetos'),
    url(r'^api/atividades/$', AtividadesView.as_view(), name='atividades'),
    url(r'^api/perfis/$', PerfilView.as_view(), name='perfis')
]
