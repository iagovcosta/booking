from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=30)
    senha =  models.CharField(max_length=10)
    tipo = models.CharField(max_length=9)

    def __str__(self):
        return self.nome