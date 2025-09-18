from django.contrib import admin
from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'preco_promocional', 'desconto_percentual', 'em_promocao', 'estoque', 'categoria']
    list_filter = ['em_promocao', 'categoria']
    search_fields = ['nome']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'descricao', 'preco', 'estoque', 'imagem', 'categoria')
        }),
        ('Promoção', {
            'fields': ('em_promocao', 'desconto_percentual', 'preco_promocional'),
            'description': 'Preencha APENAS UM dos campos abaixo. O outro será calculado automaticamente. Se ambos estiverem vazios, a promoção será desativada.'
        }),
    )