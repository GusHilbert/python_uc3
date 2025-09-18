from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')

    # 🔥 Campos de promoção — ADICIONE ESTES
    em_promocao = models.BooleanField(default=False, verbose_name="Está em promoção?")
    desconto_percentual = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Desconto (%)",
        help_text="Preencha para calcular automaticamente o valor promocional."
    )
    preco_promocional = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="Preço Promocional (R$)",
        help_text="Preencha para calcular automaticamente o % de desconto."
    )

    def save(self, *args, **kwargs):
        # Se desconto_percentual for preenchido → calcula preco_promocional
        if self.desconto_percentual is not None and self.desconto_percentual > 0:
            if self.desconto_percentual > 100:
                self.desconto_percentual = 100  # limita a 100%
            desconto = self.preco * (self.desconto_percentual / 100)
            self.preco_promocional = self.preco - desconto
        # Se preco_promocional for preenchido → calcula desconto_percentual
        elif self.preco_promocional is not None and self.preco_promocional > 0:
            if self.preco_promocional >= self.preco:
                self.preco_promocional = self.preco  # não permite promoção acima do preço original
                self.desconto_percentual = 0
            else:
                desconto = self.preco - self.preco_promocional
                self.desconto_percentual = (desconto / self.preco) * 100
        else:
            # Se nenhum for preenchido, limpa ambos
            self.desconto_percentual = None
            self.preco_promocional = None

        # Se algum campo de promoção estiver preenchido, força em_promocao=True
        if self.desconto_percentual or self.preco_promocional:
            self.em_promocao = True
        else:
            self.em_promocao = False

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome