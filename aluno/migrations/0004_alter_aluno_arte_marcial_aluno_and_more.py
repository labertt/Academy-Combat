# Generated by Django 4.1.3 on 2023-01-27 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0003_alter_aluno_arte_marcial_aluno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='arte_marcial_aluno',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='turno_aluno',
            field=models.CharField(max_length=256),
        ),
    ]
