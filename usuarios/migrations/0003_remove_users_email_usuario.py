# Generated by Django 4.1.3 on 2023-01-05 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_users_cargo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='email_usuario',
        ),
    ]