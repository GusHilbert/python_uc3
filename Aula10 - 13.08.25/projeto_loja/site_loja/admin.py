from django.contrib import admin
from django.utils.html import format_html
from .models import Perfil
from .models import Produto

admin.site.register(Perfil)
admin.site.register(Produto)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'imagem_preview')

    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="width: 100px; height:auto;" />', obj.imagem.url)
        return "-"
    imagem_preview.short_description = 'Imagem'