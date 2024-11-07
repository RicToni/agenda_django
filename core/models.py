from django.db import models

# Create your models here.

class Evento(models.Model):
    título = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)

    