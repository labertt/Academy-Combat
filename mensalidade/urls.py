from django.urls import path
from . import views

urlpatterns = [

    path('cadastrar_mensalidade/', views.cadastrar_mensalidade, name='cadastrar_mensalidade'),
    path('listagem_mensalidade/', views.listagem_mensalidade, name='listagem_mensalidade'),
   

]