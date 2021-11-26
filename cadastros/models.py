from django.db import models

# Create your models here.
# Criar todas as classes de acordo com seu diagrama de Classes
class Estado(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.sigla + ' - ' + self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    habitantes = models.IntegerField()
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + '/' + self.estado.sigla

