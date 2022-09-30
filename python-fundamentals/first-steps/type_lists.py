# Listas #
# Sendo uma coleção de itens, a lista trás inumeras possibilidades de armanzemaneto #
# Podendo armazenar String, Números ou até outras listas #
# Uma lista é indicada por [], onde os elementos são separados por virgulas #
#
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print('\nEste é um exemplo de lista: ' + str(bicycles))
print('Este é um exemplo de acesso a itens da lista -> variavel[posicao do item]: ' + str(bicycles[1]))
print('Este é um exemplo formatando a string de saida: ' + str(bicycles[2]).title())
print('Este é um exemplo pegando o ultimo item de uma lista [-1]: ' + str(bicycles[-1]).title())
#
message = 'My first bicycle was a ' + bicycles[0].title() + '.'
print('\nEste é um exemplo de mensagem formatada, pegando um item da lista: ' + message)
print('\n--')


# É possivel modificar, adicionar e remover itens de uma lista  #
# Caso nosso objetivo seja modificar, precisamos passar o nome da lista, e o indice do item que será alterado    #
#
alternative_motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles = ['honda', 'yamaha', 'suzuki']
#
motorcycles[1] = 'ducati'
print('\nIremos mudar o item 1 da lista de motocicletas, a lista possuia os itens: ' + str(alternative_motorcycles) + ', agora possui: ' + str(motorcycles))
#
# Caso nosso objetivo seja adicionar, precisamos passar o nome da lista, e utilizar a função append('item'), onde o item será adicionado no final da lista    #
#
alternative_motorcycles.append('ducati')
print('\nAdicionando uma moto a nossa lista: ' + str(alternative_motorcycles))
#
# Podemos também criar uma lista vazia, e atráves do método append() incluir quantos itens quisermos.   #
#
wallet = []
print('\nprint da lista antes de inserir os itens: ' + str(wallet))
#
wallet.append('apple pay')
wallet.append('google pay')
wallet.append('samsung pay')
print('print da lista depois de inserir os itens: ' + str(wallet))
#
# Outro caso que pode ocorrer é adicionar o novo item em um indice em especifico, podemos utilizar o método insert(indice, valor)   #
#
motorcycles = ['honda', 'yamaha', 'suzuki']
print('\nLista antes do método insert: ' + str(motorcycles))
#
motorcycles.insert(0, 'ducati')
print('Lista depois do método insert: ' + str(motorcycles))
#
# Caso nosso objetivo seja remover, e a posição do item for conhecida, podemos utilizar a função del(valor) #
# Podendo remover qualquer posição atráves do indice    #
#
motorcycles = ['honda', 'yamaha', 'suzuki']
print('\nLista antes do método del: ' + str(motorcycles))
#
del motorcycles[1]
print('Lista depois do método del: ' + str(motorcycles))
#
# Se for necessario utilizar o valor removido, o ideal é que seja utilizada a função pop()  #
# O pop remove o ultimo item da lista, ou pode-se ser passado o indice do item que será removido pop(valor) #
motorcycles = ['honda', 'yamaha', 'suzuki']
print('\nLista antes do método pop: ' + str(motorcycles))
#
popped_motorcycles = motorcycles.pop()
print('Lista com os objetos que foram removidos atráves do método pop: ' + str(popped_motorcycles))
#
# E se o indice não for conhecido, apenas o valor/nome, podemos utilizar a função remove(valor) #
# Podemos armazenar em uma váriavel o valor/nome a ser removido e passar na função  #
# Um ponto a se observar, o método remove, apenas apaga a primeira aparição daquele valor, caso seja necessario remover mais, a utilização de uma laço é necessaria #
#
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
#
motorcycles.remove(too_expensive)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')
#
print('\n--')