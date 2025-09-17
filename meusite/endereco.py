from django.db import models
from django.contrib.auth.models import User
from meusite.pessoa import Pessoa

class Endereco(models.Model):
    rua = models.CharField(max_length=150, verbose_name="Rua")
    numero = models.CharField(max_length=10, verbose_name="Número")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    complemento = models.CharField(max_length=100, blank=True, null=True, verbose_name="Complemento")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    estado = models.CharField(max_length=40, verbose_name="Estado")
    cep = models.CharField(max_length=20,verbose_name="CEP")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}"
