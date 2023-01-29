from django.shortcuts import render

def cadastrar_presenca(request):
    status = request.GET.get('status')
    return render(request, 'cadastrar_presenca.html', {'status':status})

def listagem_presenca(request):
    status = request.GET.get('status')
    return render(request, 'listar_presenca.html', {'status':status})