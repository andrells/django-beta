from django.db import models
from django.contrib.auth import get_user_model

class Produtos(models.Model):


    nome_produto = models.CharField(max_length=30)
    qnt_produto = models.IntegerField()
    valor_produto = models.FloatField(max_length=6)
    opcional = (
        ('info', 'informatica'),
        ('home', 'escritorio'),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tipo_opcional = models.CharField(max_length=10, choices=opcional)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_produto