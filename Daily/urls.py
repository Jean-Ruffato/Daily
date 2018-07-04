from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from django.contrib import admin
from Funcionarios import views

urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
    url(r'^home', views.home, name='home'),
    url(r'^encerrar', auth_views.logout, {'next_page': '/'}, name='encerrar'),
    url(r'^', include(('Funcionarios.urls', 'Funcionarios'), namespace='Funcionarios')),
    url(r'^', include(('Coordenador.urls', 'Coordenador', ), namespace='Coordenador')),
    url(r'^', include(('api.urls', 'api', ), namespace='api')),
    url(r'^', include(('Base.urls', 'Base'), namespace='Base')),
    url(r'^admin/', admin.site.urls),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
