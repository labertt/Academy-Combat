from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator
from .models import Aluno
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages

@has_permission_decorator('cadastrar_aluno')
def cadastrar_aluno(request):
    if request.method == 'GET':
        alunos = Aluno.objects.all()
        return render(request, 'cadastrar_aluno.html', {'alunos': alunos})
      
    if request.method == 'POST':
        nome_completo_aluno = request.POST.get('nome_completo_aluno')
        cpf_aluno = request.POST.get('cpf_aluno')
        data_nascimento_aluno = request.POST.get('data_nascimento_aluno')
        endereco_aluno = request.POST.get('endereco_aluno')
        email_aluno = request.POST.get('email_aluno')
        turno_aluno = request.POST.get('turno_aluno')
        arte_marcial_aluno = request.POST.get('arte_marcial_aluno')

        
        '''try:'''
        aluno = Aluno(nome_completo_aluno=nome_completo_aluno, cpf_aluno=cpf_aluno, 
        data_nascimento_aluno=data_nascimento_aluno, endereco_aluno=endereco_aluno, 
        email_aluno=email_aluno, turno_aluno=turno_aluno, arte_marcial_aluno=arte_marcial_aluno)
        aluno.save()
        '''except:
            return HttpResponse('Algo errado')'''
        

        '''user = Users.objects.filter(username=username)

        if user.exists():
            # TODO: Utilizar messages do Django
            return HttpResponse('Esse username já existe!')'''
        

        # TODO: Redirecionar com uma mensagem
        return redirect('listagem_alunos')



@has_permission_decorator('listagem_aluno')
def listagem_aluno(request):
    alunos = Aluno.objects.filter().order_by('nome_completo_aluno')
    return render(request, 'listar_aluno.html', {'alunos':alunos})


@has_permission_decorator('cadastrar_aluno')
def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    messages.add_message(request, messages.SUCCESS, 'O Aluno foi excluido!')
    return redirect('listagem_alunos')