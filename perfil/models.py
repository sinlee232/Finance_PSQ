from django.db import models
from datetime import datetime
from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0)

    def __str__(self):
        return self.categoria
    
    def total_gasto(self):
        from extrato.models import Valores
        valores = Valores.objects.filter(categoria__id = self.id).filter(data__month=datetime.now().month).filter(tipo='S')
       
        total_valor = 0
        for valor in valores:
            total_valor += valor.valor
        return total_valor
    
    def calcula_percentual_gasto_por_categoria(self):
        if self.valor_planejamento() == 0:
            return 0
        else:
            return (self.total_gasto() / self.valor_planejamento()) * 100
    
class Conta(models.Model):
    banco_choices = (
        ('NU', 'Nubank'),
        ('CE', 'Caixa econômica'),
        ('BR', 'Bradesco'),
        ('IT', 'Itaú'),
        ('C', 'C6')

    )
    tipo_choices = (
        ('pf', 'Pessoa física'),
        ('pj', 'Pessoa jurídica')
    )

    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=2, choices=banco_choices)
    tipo = models.CharField(max_length=2, choices=tipo_choices)
    valor = models.FloatField()
    icone = models.ImageField(upload_to="icones")

    def __str__(self):
        return self.apelido
    
class Despesa(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    # Outros campos do modelo de despesa

    def __str__(self):
        return f"Despesa: R$ {self.valor}"
