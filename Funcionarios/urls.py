from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^funcionarios/iniciar/(?P<pk>\d+)/$', views.iniciar, name='iniciar'),
    url(r'^funcionarios/continuar/(?P<pk>\d+)/$', views.continuar, name='continuar'),
    url(r'^funcionarios/pausar/(?P<pk>\d+)/$', views.pausar, name='pausar'),
    url(r'^funcionarios/parar/(?P<pk>\d+)/$', views.parar, name='parar'),
    url(r'^funcionarios/finalizar/(?P<pk>\d+)/$', views.finalizar, name='finalizar'),
    url(r'^funcionarios/atividades/(?P<pk>\d+)', views.atividade, name='atividade'),
    url(r'^funcionarios/pendentes', views.pendentes, name='pendentes'),
	url(r'^funcionarios/pendente/(?P<pk>\d+)', views.pendente, name='pendente'),
    url(r'^funcionarios/apagar/(?P<pk>\d+)', views.apagar, name='apagar'),
	url(r'^funcionarios/apagar_pendente/(?P<pk>\d+)', views.apagar_pendente, name='apagar_pendente'),
    url(r'^funcionarios/atividades', views.atividades, name='atividades'),
    url(r'^funcionarios', views.funcionarios, name='home'),
]
