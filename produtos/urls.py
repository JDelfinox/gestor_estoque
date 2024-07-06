"""
URL configuration for gestor_estoque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import (
    adicionar_categorias,
    adicionar_embalagens,
    adicionar_fornecedores,
    adicionar_local,
    adicionar_produtos,
    editar_categorias,
    editar_embalagens,
    editar_fornecedores,
    editar_locais,
    editar_produtos,
    excluir_categorias,
    excluir_embalagens,
    excluir_fornecedores,
    excluir_locais,
    excluir_produtos,
    inicio,
    listar_categorias,
    listar_embalagens,
    listar_fornecedores,
    listar_locais,
    listar_produtos,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('locais/', listar_locais, name='listar_locais'),
    path('locais/adicionar/', adicionar_local, name='adicionar_local'),
    path('embalagens/', listar_embalagens, name='listar_embalagens'),
    path('embalagens/adicionar/', adicionar_embalagens, name='adicionar_embalagens'),  # noqa: E501
    path('editar_locais/<pk>/', editar_locais, name='editar_locais'),
    path('editar_embalagens/<pk>/', editar_embalagens, name='editar_embalagens'),  # noqa: E501
    path('excluir_locais/<pk>/', excluir_locais, name='excluir_locais'),
    path('excluir_embalagens/<pk>/', excluir_embalagens, name='excluir_embalagens'),  # noqa: E501
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/adicionar/', adicionar_categorias, name='adicionar_categorias'),  # noqa: E501
    path('editar_categorias/<pk>/', editar_categorias, name='editar_categorias'),  # noqa: E501
    path('excluir_categorias/<pk>/', excluir_categorias, name='excluir_categorias'),  # noqa: E501
    path('fornecedores/', listar_fornecedores, name='listar_fornecedores'),
    path('fornecedores/adicionar/', adicionar_fornecedores, name='adicionar_fornecedores'),  # noqa: E501
    path('editar_fornecedores/<pk>/', editar_fornecedores, name='editar_fornecedores'),  # noqa: E501
    path('excluir_fornecedores/<pk>/', excluir_fornecedores, name='excluir_fornecedores'),  # noqa: E501
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('produtos/adicionar/', adicionar_produtos, name='adicionar_produtos'),  # noqa: E501
    path('editar_produtos/<pk>/', editar_produtos, name='editar_produtos'),  # noqa: E501
    path('excluir_produtos/<pk>/', excluir_produtos, name='excluir_produtos'),  # noqa: E501
]
