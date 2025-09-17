from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    sobrenome = models.CharField(max_length=100, verbose_name="Sobrenome")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    email = models.EmailField(max_length=100, unique=True, verbose_name="E-mail")
    telefone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefone")
    datadenascimento = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")
    rg = models.CharField(max_length=20, unique=True, verbose_name="RG")
    user = models.ForeignKey(User, on_delete=models.CASCADE,)

    def __str__(self):
        return f"Perfil de {self.user.username}"