from django.contrib import admin
from django.urls import path, include
from .views import home, listar, salvar, editar, update, deletar

urlpatterns = [
    path('', view = home, name='index'),
    path('index.html', view = home, name='index'),
    path('listagem.html', view = listar),
    path('salvar/', view = salvar, name="salvar"),
    path('editar/<int:id>', view = editar, name="editar"),
    path('update.html/<int:id>', view = update, name="update"),
    path('deletar/<int:id>', view = deletar, name="deletar"),
]
