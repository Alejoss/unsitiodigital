from django.conf.urls import url

from main import views

urlpatterns = [
		url(r'^$', views.Inicio.as_view(), name='inicio'),
		url(r'^quienes_somos/$', views.QuienesSomos.as_view(), name='quienes_somos'),
		url(r'^opciones/$', views.Opciones.as_view(), name='opciones'),
		url(r'^contacto/$', views.Contacto.as_view(), name='contacto'),
		# url(r'^mensajeenviado/$', views.MensajeEnviado.as_view(), name='mensajeenviado')
]
