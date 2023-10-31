from multiprocessing import connection
from django.shortcuts import render, redirect
from .models import Aluno


def home(request):
    return render(request, 'index.html')


def listar(request):
    alunos = Aluno.objects.all()
    return render(request, "listagem.html", {"alunos": alunos})


def salvar(request):
    nome = request.POST.get("nome")
    Aluno.objects.create(nome=nome)
    alunos = Aluno.objects.all()
    alunos = render(request, "index.html", {"alunos": alunos})
    return redirect(home)


def editar(request, id):
    aluno = Aluno.objects.get(id=id)
    return render(request, "update.html", {"aluno": aluno})


def update(request, id):
    nome = request.POST.get("nome")
    aluno = Aluno.objects.get(id=id)
    aluno.nome = nome
    aluno.save()
    return redirect(home)


def deletar(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect(home)
