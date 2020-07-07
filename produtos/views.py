from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Produtos
from .forms import ProdutosForm
from django.contrib import messages
from django.core.paginator import Paginator

def listaProdutos(request):
    search = request.GET.get('search')
    if search:
        produto = Produtos.objects.all()
    else:
        produto_list = Produtos.objects.all().order_by('-create_at')
        paginator = Paginator(produto_list, 3)
        page = request.GET.get('page')
        produto = paginator.get_page(page)

    return render(request, "produtos/index.html", {'produto': produto})



def addProdutos(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST)

        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            a.save()
            return redirect('/produtos/')
    else:
        form = ProdutosForm()
        return render(request, 'produtos/add_produto.html', {'form': form})

def produtosViews(request, id):
    produto = get_object_or_404(Produtos, pk=id)
    return render(request, 'produtos/produto.html', {'produto': produto})

def editProdutos(request, id):
    produto = get_object_or_404(Produtos, pk=id)
    form = ProdutosForm(instance=produto)

    if(request.method =='POST'):
        form = ProdutosForm(request.POST, instance=produto)
        if(form.is_valid()):
            produto.save()
            return redirect('/produtos/')
        else:
            return render(request, 'produtos/editeproduto.html.', {'form': form, 'produto': produto})
    else:
        return render(request, 'produtos/editeproduto.html', {'form': form, 'produto': produto})


def deleteProdutos(request, id):
    produto = get_object_or_404(Produtos, pk=id)
    produto.delete()
    messages.info(request, 'Produto deletado com sucesso')
    return redirect('/produtos/')



