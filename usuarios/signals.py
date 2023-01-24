from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Users
from rolepermissions.roles import assign_role

@receiver(post_save, sender=Users)
def define_permissoes(sender, instance, created, **kwargs):
    if created:
        if instance.cargo == 'Funcionario':
            assign_role(instance, 'funcionario')
        elif instance.cargo == 'Gerente':
            assign_role(instance, 'gerente')
        elif instance.cargo == 'Professor':
            assign_role(instance, 'professor')