#Faça um programa que o usuario insira 10 produtos numa tupla. Exiba todos os produtos, solicite ao usuário para digitar um nome de produto e exiba a posição dele, em seguida peça para digitar numero entre 0 e 9 e exiba o produto da tupla.
produtos = ('feijao', 'arroz', 'cafe', 'suco', 'cuscuz', 'macarrão', 'tomate', 'cebola', 'ovo', 'farinha')

print(produtos)
Nprodutos = input('Insira o nome de um produto: ')
if Nprodutos in produtos:
    Jprodutos = produtos.index(Nprodutos)
    print('O produto "{}" esta na posição "{}"'.format(Nprodutos, Jprodutos))


Pproduto = int(input('Agora digite um numero de 0 a 9: '))

if  0 <= Pproduto < len(produtos):
    print('o produto é: {}'.format(produtos[Pproduto]))
print('IsaacSouza')