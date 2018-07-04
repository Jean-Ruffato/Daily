from django.conf.urls import url
from Funcionarios.views import ProjetosView, AtividadesView

urlpatterns = [
    url(r'^api/projetos/$', ProjetosView.as_view(), name='projetos'),
    url(r'^api/atividades/$', AtividadesView.as_view(), name='atividades')
]
