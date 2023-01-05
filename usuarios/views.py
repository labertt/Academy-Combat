from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator
from .models import Users, Usuarios
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages

@has_permission_decorator('cadastrar_funcionario')
def cadastrar_funcionario(request):
    if request.method == 'GET':
        funcionarios = Users.objects.filter(cargo="Funcionario")
        return render(request, 'cadastrar_funcionario.html', {'funcionarios': funcionarios})
      
    if request.method == 'POST':
        nome_completo_usuario = request.POST.get('nome_completo_usuario')
        cpf_usuario = request.POST.get('cpf_usuario')
        data_de_nascimento_usuario = request.POST.get('data_de_nascimento_usuario')
        endereco_usuario = request.POST.get('endereco_usuario')
        email = request.POST.get('email')
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        
        try:
            user = Users.objects.create_user(username=username, password=senha, cargo="Funcionario", first_name=nome_completo_usuario, email=email, cpf_usuario=cpf_usuario, endereco_usuario=endereco_usuario)
            usuario = Usuarios(nome_completo_usuario=nome_completo_usuario, cpf_usuario=cpf_usuario, 
            data_de_nascimento_usuario=data_de_nascimento_usuario, endereco_usuario=endereco_usuario, email=email)
            user.save()
            usuario.save()
        except:
            return HttpResponse('Algo errado')
        

        '''user = Users.objects.filter(username=username)

        if user.exists():
            # TODO: Utilizar messages do Django
            return HttpResponse('Esse username já existe!')'''
        

        # TODO: Redirecionar com uma mensagem
        return redirect('listagem_funcionarios')

@has_permission_decorator('cadastrar_professor')
def cadastrar_professor(request):
    if request.method == 'GET':
        professores = Users.objects.filter(cargo="Professor")
        return render(request, 'cadastrar_professor.html', {'professores': professores})
        
    if request.method == 'POST':
        nome_completo_usuario = request.POST.get('nome_completo_usuario')
        cpf_usuario = request.POST.get('cpf_usuario')
        data_de_nascimento_usuario = request.POST.get('data_de_nascimento_usuario')
        endereco_usuario = request.POST.get('endereco_usuario')
        email = request.POST.get('email')
        username = request.POST.get('username')
        senha = request.POST.get('senha')
     

        user = Users.objects.filter(username=username)

        if user.exists():
            # TODO: Utilizar messages do Django
            return HttpResponse('Esse username já existe!')

        try:
            user = Users.objects.create_user(username=username, password=senha, cargo="Professor", first_name=nome_completo_usuario, email=email, cpf_usuario=cpf_usuario, endereco_usuario=endereco_usuario)
            usuario = Usuarios(nome_completo_usuario=nome_completo_usuario, cpf_usuario=cpf_usuario, 
            data_de_nascimento_usuario=data_de_nascimento_usuario, endereco_usuario=endereco_usuario, email=email)
            user.save()
            usuario.save()
        except:
            return HttpResponse('Esse username já existe!')
        

        # TODO: Redirecionar com uma mensagem
        return redirect('listagem_professores')

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('plataforma'))
        return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            return HttpResponse('Usuário Inválido')

        auth.login(request, user)
        return redirect('home')

def logout(request):
    request.session.flush()
    return redirect(reverse(login))

@has_permission_decorator('listagem_funcionario')
def listagem_funcionario(request):
    funcionarios = Users.objects.filter(cargo="Funcionario").order_by('first_name')
    return render(request, 'listar_funcionario.html', {'funcionarios':funcionarios})

@has_permission_decorator('listagem_professor')
def listagem_professor(request):
    professores = Users.objects.filter(cargo="Professor").order_by('first_name')
    return render(request, 'listar_professor.html', {'professores':professores})

@has_permission_decorator('cadastrar_funcionario')
def excluir_usuario(request, id):
    funcionario = get_object_or_404(Users, id=id)
    funcionario.delete()
    messages.add_message(request, messages.SUCCESS, 'O funcionário foi excluido!')
    return redirect('listagem_funcionarios')

@has_permission_decorator('cadastrar_professor')
def excluir_usuario(request, id):
    funcionario = get_object_or_404(Users, id=id)
    funcionario.delete()
    messages.add_message(request, messages.SUCCESS, 'O professor foi excluido!')
    return redirect('listagem_professores')