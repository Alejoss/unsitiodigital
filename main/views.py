from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy


from forms import FormContacto


class Inicio(TemplateView):
	template_name = "inicio.html"


class QuienesSomos(TemplateView):
	template_name = "quienes_somos.html"


class Opciones(TemplateView):
	template_name = "opciones.html"


class Contacto(FormView):
	template_name = "contacto.html"
	form_class = FormContacto
	success_url = reverse_lazy('main:mensaje_enviado')

	def form_valid(self, form):
		
		form.send_email()
		return super(Contacto, self).form_valid(form)


class MensajeEnviado(TemplateView):
	template_name = "mensaje_enviado.html"
