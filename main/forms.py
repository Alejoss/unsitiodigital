from django import forms
from django.forms import TextInput, Textarea, CheckboxInput
from django.core.mail import send_mail


class FormContacto(forms.Form):
	tema = forms.CharField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
	mensaje = forms.CharField(max_length=500, widget=Textarea(attrs={'class': 'form-control'}))
	email = forms.EmailField(max_length=100, widget=TextInput(attrs={'class': 'form-control'}))
	enviar_copia = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class': 'form-control'}))

	def enviar_mail(self):
		tema = self.cleaned_data["tema"]
		mensaje = self.cleaned_data["mensaje"]
		email = self.cleaned_data["email"]
		enviar_copia = self.cleaned_data["enviar_copia"]
		receptores = ["alejoveintimilla@gmail.com"]
		if enviar_copia:
			receptores += "email"

		send_mail(
			subject=tema,
			message=mensaje,
			from_email=email,
			receptores=receptores
			)
