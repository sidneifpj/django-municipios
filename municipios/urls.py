# Alterado para o django 1.10
try:
    from django.conf.urls import url
except:
    from django.conf.urls.defaults import url
    
from municipios.views import base_url_js, municipios_ajax, teste

urlpatterns = [
    url(r'^$', base_url_js, name='municipios-base-url'),
    url(r'^base_url.js$', base_url_js, name='municipios-base-url-js'),
    url(r'^ajax/municipios/(?P<uf>\w\w)/(?P<app_label>\w+)/(?P<object_name>\w+)/$', municipios_ajax, name='municipios-ajax'),
    url(r'^teste/', teste, name='municipios-teste'),
]
