from multiprocessing import connection
from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
