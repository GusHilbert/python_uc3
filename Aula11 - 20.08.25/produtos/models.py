# produtos/models.py (aula 10)

from django.db import models
from django.contrib.auth.models import User # Importa o modelo de usuário padrão do Django
from PIL import Image # Importa o Image para redimensionar a imagem

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem = models.ImageField(default='perfil_padrao.jpg', upload_to='imagens_perfil')
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # Salva a imagem primeiro

        img = Image.open(self.imagem.path) # Abre a imagem
        if img.height > 300 or img.width > 300: # Verifica se é maior que 300x300 pixels
            output_size = (300, 300)
            img.thumbnail(output_size) # Redimensiona a imagem
            img.save(self.imagem.path) # Salva a imagem redimensionada


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True) # Campo para imagem

    def __str__(self):
        return self.nome

        from django.db import models
