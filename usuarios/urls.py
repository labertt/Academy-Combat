from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name="cadastrar_funcionario"),
    path('cadastrar_professor/', views.cadastrar_professor, name="cadastrar_professor"),
    path('login/', views.login, name="login"),
    path('listagem/', views.listagem, name='listagem'),
    path('listagem_funcionarios/', views.listagem_funcionario, name='listagem_funcionarios'),
    path('listagem_professores/', views.listagem_professor, name='listagem_professores'),
    path('logout/', views.logout, name="logout"),
    path('excluir_usuario/<str:id>/', views.excluir_usuario, name="excluir_usuario")
]