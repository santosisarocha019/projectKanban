from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.nome


class Prioridade(models.TextChoices):
    BAIXO = 'Baixo'
    MEDIA = 'Media'
    ALTA = 'Alto'

class Status(models.TextChoices):
    FAZER = "A fazer"
    FAZENDO = "Fazendo"
    PRONTO = "Pronto"

class Tarefa(models.Model):
    
    descricao = models.CharField(max_length=255, null=False)
    nome_setor = models.CharField(max_length=255, null=False)
    prioridade = models.CharField(max_length=10, choices=Prioridade.choices)
    data_cadastro = models.DateField( auto_now_add=True)
    status = models.CharField(max_length=10, choices=Status.choices, default = Status.FAZER)
    id_usuario = models.ForeignKey('Usuario', related_name='id_usuario', on_delete=models.CASCADE, null= False)

    def __str__(self):
        return self.descricao
    
    
# Create your models here.
