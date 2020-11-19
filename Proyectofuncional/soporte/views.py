from django.shortcuts import render
from django.core.mail import send_mail
from operator import attrgetter
from django.conf import settings
from soporte.forms import FormularioContacto

# Create your views here.

def soporte_pag(request):
	if request.method=="POST":
		miFormulario=FormularioContacto(request.POST)

		if miFormulario.is_valid():
			infForm=miFormulario.cleaned_data
			send_mail(infForm['asunto'],infForm['mensaje'], 
			infForm.get('email', ''),['aillnovotech@gmail.com'],)
			return render(request, "gracias.html")

	else:
		miFormulario=FormularioContacto()

	return render(request, "formulario_contacto.html", {"form": miFormulario})