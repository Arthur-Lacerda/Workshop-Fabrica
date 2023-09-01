from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=50)

    
    def __str__(self):
        return f"Nome do Livro: {self.nome}"

class Loja(models.Model):
    autor = models.CharField(max_length=30)
    preco = models.CharField(max_length=10)
    nome = models.ForeignKey(
        Livro,
        max_length = 20,
        on_delete=models.CASCADE
    )