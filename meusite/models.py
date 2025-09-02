from django.db import models
 
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    datadenascimento = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")
    rg = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=150, blank=True, null=True, verbose_name="Endereço")
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.nome

# Create your models here.
