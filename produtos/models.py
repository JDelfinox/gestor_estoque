from django.db import models

from utils.base_models import BaseModel


class Categoria(BaseModel):
    nome = models.CharField(
        max_length=100, verbose_name='Nome da categoria', unique=True
    )  # noqa: E501

    class Meta:
        db_table = 'categorias'

    def __str__(self) -> str:
        return f"{self.nome}"


class Produto(BaseModel):
    nome = models.CharField(max_length=100, verbose_name='nome do produto')
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        verbose_name='categoria do produto',
    )  # noqa: E501
    embalagens = models.ManyToManyField(
        'produtos.Embalagem', verbose_name='Embalagens do Produtos'
    )  # noqa: E501
    estoque_minimo = models.FloatField(
        verbose_name='Estoque Minimo do Produto'
    )
    estoque_maximo= models.FloatField(
        verbose_name='Estoque Máximo do Produto'
    )
    class Meta:
        db_table = 'produtos'


class Fornecedor(BaseModel):
    nome_social = models.CharField(
        max_length=100, verbose_name='Nome Social do Fornecedor', unique=True
    )  # noqa: E501
    nome_fantasia = models.CharField(
        max_length=100, verbose_name='Nome Fantasia do Fornecedor'
    )  # noqa: E501
    produtos = models.ManyToManyField(
        'produtos.Produto', verbose_name='Produtos do Fornecedor'
    )  # noqa: E501

    class Meta:
        db_table = 'fornecedores'


class Embalagem(BaseModel):
    nome = models.CharField(max_length=50, verbose_name='Nome da embalagem')  # noqa: F811
    sigla = models.CharField(max_length=3, verbose_name='Sigla da embalagem')

    class Meta:
        db_table = 'embalagens'

    def __str__(self) -> str:
        return f"{self.nome} - {self.sigla}"


class Movimentacao(BaseModel):
    TIPOS_MOVIMENTACAO = [(1, 'Entrada'), (-1, 'Saída')]
    fornecedor = models.ForeignKey(
        'produtos.Fornecedor',
        on_delete=models.CASCADE,
        verbose_name='Fornecedor do produto armazenado',
    )  # noqa: E501
    produto = models.ForeignKey(
        'produtos.Produto',
        on_delete=models.CASCADE,
        verbose_name='produto da movimentação',
    )  # noqa: E501
    quantidade = models.DecimalField(
        max_digits=10, decimal_places=6, verbose_name='Quantidade Movimentada'
    )  # noqa: E501
    local = models.ForeignKey(
        'produtos.local',
        on_delete=models.CASCADE,
        verbose_name='Local da Movimentação',
    )  # noqa: E501

    tipo = models.IntegerField(
        choices=TIPOS_MOVIMENTACAO, verbose_name='Tipo de Movimentação'
    )  # noqa: E501

    preco = models.DecimalField(
        max_digits=10,
        decimal_places=6,
        verbose_name='Preço do Produto na Movimentação',
    )
    codigo_fabricante = models.CharField(
        max_length=20,
        verbose_name='Código do Fabricante',
    )

    class Meta:
        db_table = 'movimentacoes'


class Local(BaseModel):
    TIPOS_DE_LOCAL = [('F', 'Fisico'), ('D', 'Digital')]
    nome = models.CharField(
        max_length=50, verbose_name='nome do local armazenado', unique=True
    )  # noqa: E501
    tipo = models.CharField(
        max_length=1,
        choices=TIPOS_DE_LOCAL,
        verbose_name='Tipo de local armazenado',
    )  # noqa: E501

    class Meta:
        db_table = 'locais'
