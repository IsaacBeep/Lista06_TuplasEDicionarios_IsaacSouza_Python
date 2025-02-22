#Peça ao usuário para inserir os nomes de três pessoas que deseja convidar para uma festa e armazená-las em uma lista. Depois de inserir os três nomes, pergunte se deseja adicionar outro. Se o fizer, permita que adicione mais nomes até responder "não". Quando ele responder "não", mostre quantas pessoas ele convidou para a festa, uma vez que o usuário tenha completado sua lista de nomes, 
#exiba a lista completa e peça que ele digite um dos nomes da lista. Exiba a posição desse nome na lista. Pergunte ao usuário se ele ainda deseja que essa pessoa venha à festa. Se ele responder "não", exclua essa entrada da lista e exiba a lista novamente.
festa = []

for contador in range(0, 3):
    Lfesta = input('Digite o nome da pessoa que deseja convidar para a festa: ')
    festa.append(Lfesta)

Dfesta = input('Você convidou {} pessoas< deseja convidar mais pessoas? s/n:'.format(festa)).lower()
if Dfesta == 's':
    while True:
        LfestaR = input('Digite o nome da pessoa que deseja convidar para a festa: ')
        festa.append(LfestaR)
        Dfesta = input('Deseja convidar mais pessoas? s/n:')
        if Dfesta == 'n':
            break
        else:
            break
else:
    print('Ok, continue')
print(festa)

Nlista = input('Agora digite um nome da lista: ')

if Nlista in festa:
    Clista = festa.index(Nlista)
    print('A Pessoa convidada esta na posição "{}"'.format(Clista))
    CPfesta = input('Ainda deseja que ele compareça na festa? s/n: ')
    if CPfesta == 's':
        print('Ok ')
    elif CPfesta == 'n':
        festa.remove(CPfesta)
        print(festa)

print('IsaacSouza')

   