from django.contrib import admin
from meusite.pessoa import Pessoa
from meusite.endereco import Endereco

admin.site.register(Endereco)
admin.site.register(Pessoa)
# Register your models here.
