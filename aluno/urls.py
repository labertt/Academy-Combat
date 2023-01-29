from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_aluno/', views.cadastrar_aluno, name="cadastrar_aluno"),
    path('listagem_alunos/', views.listagem_aluno, name='listagem_alunos'),
    path('excluir_aluno/<str:id>/', views.excluir_aluno, name="excluir_aluno")
]