from django.urls import path
from . import views

urlpatterns = [

    path('cadastrar_presenca/', views.cadastrar_presenca, name='cadastrar_presenca'),
    path('listagem_presenca/', views.listagem_presenca, name='listagem_presenca'),
   

]