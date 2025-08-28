from django.shortcuts import render
from .models import Produto

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/home.html', {'produtos': produtos})
