from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    título = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.título
    
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')