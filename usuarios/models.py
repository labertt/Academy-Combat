from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    cargos = (
        ('G', 'Gerente'),
        ('F', 'Funcionario'),
        ('P', 'Professor')
    )
    cargo = models.CharField(max_length=1, choices=cargos)

    cpf_usuario = models.CharField(max_length=11, unique=True)
    email_usuario = models.CharField(max_length=256, unique=True)


class Usuarios(models.Model):
    nome_completo_usuario = models.CharField(max_length=100)
    cpf_usuario = models.CharField(max_length=11, unique=True)
    data_de_nascimento_usuario = models.DateField()
    endereco_usuario = models.CharField(max_length=200)
    email_usuario = models.CharField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.nome_completo_usuario
