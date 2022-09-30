# Hora de exercitar os conceitos.   #
print('\nExercitando o conhecimento em listas:')
#
print('\nArmazene nomes em uma lista, e exiba os nomes um de cada vez:')
#
friends_name = ['Azriel', 'Cassian', 'Mor', 'Amren', 'Feyre']
print('\tEste é o primeiro nome de um(a) amigo(a) da lista: ' + str(friends_name[0]).title())
print('\tEste é o segundo nome de um(a) amigo(a) da lista: ' + str(friends_name[1]).title())
print('\tEste é o terceiro nome de um(a) amigo(a) da lista: ' + str(friends_name[2]).title())
print('\tEste é o quarto nome de um(a) amigo(a) da lista: ' + str(friends_name[-2]).title())
print('\tEste é o ultimo nome de um(a) amigo(a) da lista: ' + str(friends_name[-1]).title())
#
#
print('\nExiba uma mensagem personalizada, passando os nomes da lista dos amigos:')
print('\tOlá meu amigo ' + str(friends_name[0]).title() + ', a planta está ti procurando.' )
print('\tOpa meu irmão ' + str(friends_name[1]).title() + ', bão? Comprei uma garrafa de vinho pra você, mas só pode tomar a noite.')
print('\tBom dia, ' + str(friends_name[2]).title() + ' você está com uma cara horrivel hoje, quer comprar algo para melhorar?')
print('\tMinha amiga ' + str(friends_name[-2]).title() + ', comprei esse colar aqui que você vai amar!')
print('\tComprei tinta e quadros novos, ' + str(friends_name[-1]).title() + ' querida.')
#
#
print('\nCrie uma lista propria, e após isso exiba algumas frases com os itens dela:')
#
favorite_foods = ['Pizza', 'Lasanha','Macarrão com Atum']
print('\tMeu consagrado, desce uma ' + str(favorite_foods[0] + ' de camarão, atum, bahiana e de lombinho'))
print('\tNunca mais comi uma ' + str(favorite_foods[1]))
print('\t' + str(favorite_foods[-1] + ' é a minha comida mais mais mais mais mais favorita de tooodas!'))
#
#
print('\nCrie uma lista de pessoas (Mortas ou Vivas), para um jantar, e exiba o convite:')
#
invited = ['Michael Jackson', 'MC Poze', 'FunkyBlackCat']
print('\t' + invited[0] + ', venho por meio deste convida-lo, para um jantar.')
print('\t' + invited[1] + ', venho por meio deste convida-lo, para um jantar.')
print('\t' + invited[-1] + ', venho por meio deste convida-lo, para um jantar.')
#
#
print('\nUma das pessoas não poderá vir para o jantar, exiba o nome, substitua o nome da pessoa da lista:')
#
print('\tAntiga lista de convidados: ' + str(invited))
#
invited[0] = 'Perla'
print('\tNova lista de convidados: ')
print('\t' + invited[0] + ', venho por meio deste convida-la, para um jantar.')
print('\t' + invited[1] + ', venho por meio deste convida-lo, para um jantar.')
print('\t' + invited[-1] + ', venho por meio deste convida-lo, para um jantar.')
#
#
print('\nTeremos mais pessoas para o jantar, exiba o nome dos novos convidados, ' + 'Antiga lista de convidados: ' + str(invited))
#
invited.insert(0, 'Henry Cavill')
invited.insert(2, 'Ana de Armas')
invited.append('Angela Bassett')
print('\t' + invited[0] + ', venho por meio deste convida-lo, para um jantar.')
print('\t' + invited[1] + ', venho por meio deste convida-la, para um jantar.')
print('\t' + invited[2] + ', venho por meio deste convida-la, para um jantar.')
print('\t' + invited[-3] + ', venho por meio deste convida-lo, para um jantar.')
print('\t' + invited[-2] + ', venho por meio deste convida-lo, para um jantar.')
print('\t' + invited[-1] + ', venho por meio deste convida-la, para um jantar.')
#
#
print('\nDeu ruim não teremos mesa para mais pessoas, vamos ter que cancelar os convites.')
#
print('\tInfelizmente só poderemos convidar apenas 2 pessoas, a mesa não chegou, e por isso terei que cancelar com vocês.')
#
print('\tSinto muito, ' + invited.pop() + ', em ti mandar essa mensagem, mas terei que ti remover da lista de convidados, espero que não fique chateado!')
print('\tSinto muito, ' + invited.pop() + ', em ti mandar essa mensagem, mas terei que ti remover da lista de convidados, espero que não fique chateado!')
print('\tSinto muito, ' + invited.pop() + ', em ti mandar essa mensagem, mas terei que ti remover da lista de convidados, espero que não fique chateado!')
print('\tSinto muito, ' + invited.pop() + ', em ti mandar essa mensagem, mas terei que ti remover da lista de convidados, espero que não fique chateado!')
#
del invited[0]
del invited[0]
print('\tNossa lista atual é:' + str(invited))
#
#