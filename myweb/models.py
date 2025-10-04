from django.db import models

# Create your models here.
class Animal(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=100, blank=True)
    idade = models.PositiveIntegerField(null=True, blank=True)
    cor = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome