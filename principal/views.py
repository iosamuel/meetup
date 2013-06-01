from django.shortcuts import render, redirect
from .models import *
from .forms import *
#from tornado import template

def index(request):
	eventos = Eventos.objects.all().order_by('-id')
	ctx = {'eventos':eventos}
	return render(request, 'index.html', ctx)

def agregar_evento(request):
	if request.method == 'POST':
		entradas_form = EventosForm(request.POST)
		if entradas_form.is_valid():
			entradas_form.save()
			return redirect('/')
	else:
		entradas_form = EventosForm()
	ctx = {'entradas_form':entradas_form}
	# template.Context(ctx)
	# return template.render('')
	return render(request, 'agregar_evento.html', ctx)

def evento(request, id):
	evento = Eventos.objects.get(pk=id)
	if request.method == 'POST':
		usuarios_form = UsuariosForm(request.POST)
		if usuarios_form.is_valid():
			usuario = usuarios_form.save(commit=False)
			usuario.eventos = evento
			usuario.save()
			return redirect('/')
	else:
		usuarios_form = UsuariosForm()
	ctx = {'evento':evento, 'usuarios_form':usuarios_form}
	return render(request, 'evento.html', ctx)