# Generated by Django 4.1.3 on 2023-01-05 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_rename_email_usuario_usuarios_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
