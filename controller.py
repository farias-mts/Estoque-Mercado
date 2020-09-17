from model import *
import re

def novo_produto(produto, categoria, qtde):
    tipo = categoria
    categoria = str(buscar_categorias_id(categoria))
    for char in "(',)":
        categoria = categoria.replace(char, '')
    inserir_produto(produto, int(categoria), int(qtde))

def nova_categoria(categoria):
    inserir_categoria(categoria)

def buscar_produto(produto):
    for char in '*':
        produto = produto.replace(char, '%')
    lista = buscar(produto)
    return lista

def retornar_categorias():
    tipos = buscar_categorias()
    lista = []
    for item in tipos:
        lista.append(str(item))
    data = []
    for item in lista:
        for char in "(',)":
            item = item.replace(char, '')
        data.append(item)
    return data

