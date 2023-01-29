from django.db import models

class Aluno(models.Model):

    '''artes_marciais = (
        ('Kung Fu', 'Kung Fu'),
        ('Karatê', 'Karatê'),
        ('Judô', 'Judô'),
        ('Jiu-Jitsu', 'Jiu-Jitsu'),
        ('Muay Thai', 'Muay Thai'),
        ('Taekwondo', 'Taekwondo')
    )

    turnos = (
        ('Matutino', 'Matutino'),
        ('Vespertino', 'Vespertino'),
        ('Noturno', 'Noturno')
    )'''

    nome_completo_aluno = models.CharField(max_length=256)
    cpf_aluno = models.CharField(unique=True, max_length=11)
    data_nascimento_aluno = models.DateField()
    endereco_aluno = models.CharField(max_length=256)
    email_aluno = models.EmailField()
    turno_aluno = models.CharField(max_length=256)
    arte_marcial_aluno = models.CharField(max_length=256)

    def __str__(self) -> str:
        return str(self.nome_completo_aluno)