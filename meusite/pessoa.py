from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    datadenascimento = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")
    rg = models.CharField(max_length=20, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Perfil de {self.user.username}"