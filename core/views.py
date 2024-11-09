from django.shortcuts import render
from core.models import Evento

# Create your views here.
def lista_eventos(request):
    usuario = request.user # Define o usuário que realizou a solicitação.
    eventos = Evento.objects.filter(usuario=usuario) # Filtra dentre os eventos, apenas o evento do usuário que fez a requisição. 
    response = {'eventos': eventos }
    return render(request, 'agenda.html', response)