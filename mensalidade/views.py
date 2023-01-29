from django.shortcuts import render

def cadastrar_mensalidade(request):
    status = request.GET.get('status')
    return render(request, 'cadastrar_mensalidade.html', {'status':status})

def listagem_mensalidade(request):
    status = request.GET.get('status')
    return render(request, 'listar_mensalidade.html', {'status':status})