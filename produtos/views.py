from django.shortcuts import redirect, render

from .forms import (
    CategoriaForm,
    EmbalagemForm,
    FornecedorForm,
    LocalForm,
    ProdutosForm,
)
from .models import Categoria, Embalagem, Fornecedor, Local, Produto


def inicio(request):
    return render(request, 'menu.html')


def listar_locais(request):
    consulta = request.GET.get('q')
    tipo = request.GET.get('tipo')
    locais = Local.objects.all()
    if consulta:
        locais = locais.filter(nome__icontains=consulta)
    if tipo:
        locais = locais.filter(tipo=tipo)
    return render(request, 'produtos/listar_locais.html', {'locais': locais})


def adicionar_local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_locais')
    else:
        form = LocalForm()
    return render(request, 'produtos/adicionar_local.html', {'form': form})


def listar_embalagens(request):
    consulta = request.GET.get('q')
    sigla = request.GET.get('sigla')
    embalagens = Embalagem.objects.all()
    if consulta:
        embalagens = embalagens.filter(nome__icontains=consulta)
    if sigla:
        embalagens = embalagens.filter(sigla=sigla)
    return render(request, 'produtos/listar_embalagens.html', {'embalagens': embalagens})  # noqa: E501


def adicionar_embalagens(request):
    if request.method == 'POST':
        form = EmbalagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_embalagens')
    else:
        form = EmbalagemForm()
    return render(request, 'produtos/adicionar_embalagens.html', {'form': form})


def editar_locais(request, pk):
    local = Local.objects.get(pk=pk)
    if request.method == 'POST':
        form = LocalForm(request.POST, instance=local)
        if form.is_valid():
            form.save()
            return redirect('listar_locais')
    else:
        form = LocalForm(instance=local)
    return render(request, 'produtos/editar_locais.html', {'form': form, 'local': local})


def editar_embalagens(request, pk):
    embalagens = Embalagem.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmbalagemForm(request.POST, instance=embalagens)
        if form.is_valid():
            form.save()
            return redirect('listar_embalagens')
    else:
        form = EmbalagemForm(instance=embalagens)
    return render(request, 'produtos/editar_embalagens.html', {'form': form, 'embalagens': embalagens})  # noqa: E501


def excluir_locais(request, pk):
    local = Local.objects.get(pk=pk)
    local.delete()
    return redirect('listar_locais')


def excluir_embalagens(request, pk):
    embalagens = Embalagem.objects.get(pk=pk)
    embalagens.delete()
    return redirect('listar_embalagens')


def listar_categorias(request):
    consulta = request.GET.get('q')
    categorias = Categoria.objects.all()
    if consulta:
        categorias = categorias.filter(nome__icontains=consulta)
    return render(request, 'produtos/listar_categorias.html', {'categorias': categorias})  # noqa: E501


def adicionar_categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'produtos/adicionar_categorias.html', {'form': form})  # noqa: E501


def editar_categorias(request, pk):
    categorias = Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categorias)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categorias)
    return render(request, 'produtos/editar_categorias.html', {'form': form, 'categorias': categorias})  # noqa: E501


def excluir_categorias(request, pk):
    local = Categoria.objects.get(pk=pk)
    local.delete()
    return redirect('listar_categorias')


def listar_fornecedores(request):
    consulta = request.GET.get('q')
    fornecedores = Fornecedor.objects.all()
    if consulta:
        fornecedores = fornecedores.filter(nome__icontains=consulta)
    return render(request, 'produtos/listar_fornecedores.html', {'fornecedores': fornecedores})  # noqa: E501


def adicionar_fornecedores(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_fornecedores')
    else:
        form = FornecedorForm()
    return render(request, 'produtos/adicionar_fornecedores.html', {'form': form})  # noqa: E501


def editar_fornecedores(request, pk):
    fornecedores = Fornecedor.objects.get(pk=pk)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedores)
        if form.is_valid():
            form.save()
            return redirect('listar_fornecedores')
    else:
        form = FornecedorForm(instance=fornecedores)
    return render(request, 'produtos/editar_categorias.html', {'form': form, 'fornecedores': fornecedores})  # noqa: E501


def excluir_fornecedores(request, pk):
    local = Fornecedor.objects.get(pk=pk)
    local.delete()
    return redirect('listar_fornecedores')


def listar_produtos(request):
    consulta = request.GET.get('q')
    produtos = Produto.objects.all()
    if consulta:
        produtos = produtos.filter(nome__icontains=consulta)
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})  # noqa: E501


def adicionar_produtos(request):
    if request.method == 'POST':
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutosForm()
    return render(request, 'produtos/adicionar_produtos.html', {'form': form})  # noqa: E501


def editar_produtos(request, pk):
    produtos = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProdutosForm(request.POST, instance=produtos)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutosForm(instance=produtos)
    return render(request, 'produtos/editar_produtos.html', {'form': form, 'fornecedores': produtos})  # noqa: E501


def excluir_produtos(request, pk):
    local = Produto.objects.get(pk=pk)
    local.delete()
    return redirect('listar_produtos')
