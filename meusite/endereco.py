from django.db import models
from django.contrib.auth.models import User
from meusite.pessoa import Pessoa

class Endereco(models.Model):
    rua = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=40)
    cep = models.CharField(max_length=20)
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

def __str__(self):
    return f"{self.rua}, {self.bairro}, {self.cidade} - {self.estado}"
