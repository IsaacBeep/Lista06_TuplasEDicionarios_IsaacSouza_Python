#Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja, posição na lista) desse item na tupla
paises = ('brasil', 'chile', 'argentina', 'Estados Unidos', 'espanha')
print(paises)

paisE = input('Digite um pais que esta na lista: ')


if paisE in paises:
    paise = paises.index(paisE)
    print('O pais "{}" esta na lista e esta na indice "{}"'.format(paisE, paise))
else:
    print('País não está na lista')
print('IsaacSouza')