from django.db import models

# Create your models here.

class Fotografia(models.Model):
    
    OPCOES_CATEGORA = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta'),
    ]
    
    
    nome = models.CharField(max_length=100, null = False, blank = False)
    legenda = models.CharField(max_length=150, null=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORA, default='')
    descricao = models.TextField(null = False, blank=False)
    foto = models.CharField(max_length=100, null = False, blank = False)
    
    def __str__(self):
        return f"Fotografia [nome = {self.nome}]"
    
    
