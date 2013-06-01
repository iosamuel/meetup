from django import forms
from .models import *

class EventosForm(forms.ModelForm):
	class Meta:
		model = Eventos
		# widgets = {
		# 	'nombre': forms.InputText(attrs={'class':'inputB inputA'})
		# }
		# <input class="inputA inputB">

class UsuariosForm(forms.ModelForm):
	class Meta:
		model = Usuarios
		exclude = ('eventos',)