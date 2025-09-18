# views.py
from django.shortcuts import render
from .models import Produto, Categoria

def home(request):
    # Pega todas as categorias
    categorias = Categoria.objects.all()

    # Verifica se um ID de categoria foi passado na URL
    categoria_id = request.GET.get('categoria_id')  # 'categoria_id' vem da query string da URL

    # Se categoria_id for fornecido, filtra os produtos dessa categoria
    if categoria_id:
        produtos = Produto.objects.filter(categoria_id=categoria_id)
    else:
        produtos = Produto.objects.all()  # Caso contrário, mostra todos os produtos

    # Filtra e ordena promoções pela maior porcentagem de desconto
    produtos_em_promocao = Produto.objects.filter(em_promocao=True).order_by('-desconto_percentual')

    return render(request, 'loja/home.html', {
        'produtos': produtos,
        'produtos_em_promocao': produtos_em_promocao,
        'categorias': categorias,  # Passa a lista de categorias para o template
    })
