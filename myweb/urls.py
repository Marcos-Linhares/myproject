from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar/', views.cadastro_animal, name='cadastro'),
    path('editar/<int:pk>/', views.editar_animal, name='editar'),
    path('excluir/<int:pk>/', views.excluir_animal, name='excluir'),
    path('animal/<int:pk>/', views.detalhes_animal, name='detalhes'),
]