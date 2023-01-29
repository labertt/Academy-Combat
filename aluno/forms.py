from django import forms
from django.db.models import fields
from .models import Aluno
from django.db import models    
from datetime import date


class CadastroAluno(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"