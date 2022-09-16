# Strings #

# Utilizando métodos para formatação de uma string  #
# O método title() exibe cada palavra com a letra inicial sendo maiúsculas   #
# O método upper() exibe cada palavra com todas as letras sendo maiúsculas   #
# o método lower() exibe cada palabra com todas as letras sendo minúsculas   #
name = 'gandalf, o cinzento'

print(name.title())
print(name.upper())
print(name.lower())

# Utilizando o (+) para combinar (concatenar) diferentes strings #
# Podemos utilizar a concatenação para criar mensagens simples e elegantes #
first_name = 'gandalf'
last_name = 'o cinzento'
full_name = first_name + ", " + last_name

message = "Hello, " + full_name.title() + "!"

print(message)

# Podemos utilizar também tabulações e quebras de linhas #
# \t: Tabulação #
# \n: Quebra de linha   #
print("\nMercado: \n\tArroz\n\tFeijão\n\tNescau")

# Podemos também remover espaços em branco que não queremos #
# .rstrip(): Remove espaços em branco a direita #
# .lstrip(): Remove espaços em branco a esquerda    #
# .strip(): Remove espaços em branco de ambos os lados  #

right_to_space = 'Este texto possuia um espaço em branco a direta '
left_to_space = ' Este texto possuia um espaço em branco a esquerda'
space_both_sides = ' Este texto possui espaço em branco de ambos os lados '

print('\nEste é o texto original: ' + right_to_space + ', Este é o texto com a correção: ' + right_to_space.rstrip() + "!")
print('Este é o texto original: ' + left_to_space + ', Este é o texto com a correção: ' + left_to_space.lstrip() + "!")
print('Este é o texto original: ' + space_both_sides + ', Este é o texto com a correção: ' + space_both_sides.strip() + "!")

# Um Ponto muito importante de entendermos é relacionado a aspas simples e duplas #
# Caso exista dentro do texto um apóstrofo o ideal é que se utilize a ("") #

print('\nNesse caso, o ideal é se utilizar as aspas duplas: ' + "One of Python's strengths is its diverse community.")

print('\nExercitando o conhecimento:')

# Armazenando dados em uma variável #

exemplo_first_name = 'Jack'
exemplo_last_name = 'Sparrow'
exemplo_message = 'Não quis esperar, mas o ' + exemplo_first_name + ' ' +  exemplo_last_name

print('\tArmazenando um nome de uma pessoa e exibindo uma mensagem pessoal: ' + exemplo_message + '.')

print('\tArmazenando um nome de uma pessoa e exibindo em minúsculo, maiúsculo, e apenas com as primeiras letras:')
print('\t\tMinúsculo: ' + exemplo_first_name.lower())
print('\t\tMaiúsculo: ' + exemplo_first_name.upper())
print('\t\tPrimeiras letras maiúsculas: ' + exemplo_first_name.title())

print('\tExibindo uma citação famosa e alternando as aspas: ' + 'Abraham Lincoln certa vez disse: "No final das contas, não são os anos de sua vida que contam. É a vida em seus anos."')

famous_person = 'Abraham Lincoln'
famous_citation = '"No final das contas, não são os anos de sua vida que contam. É a vida em seus anos."'
famous_message = famous_person + ' certa vez disse: ' + famous_citation

print('\tArmazenando uma citação famosa e alternando as aspas: ' + famous_message)

right_to_space_name = 'Gandalf, O Cinzento '
left_to_space_name = ' Gandalf, O Cinzento'
space_both_sides_name = ' Gandalf, O Cinzento ' 

print('\tArmaze o nome em uma variável com espaços em branco ao lado direito, esquerdo e em ambos, e exiba o dado original, e após a remoção do espaço em branco:')
print('\t\tEste é o texto original: ' + right_to_space_name + ', Este é o texto com a correção: ' + right_to_space_name.rstrip() + "!")
print('\t\tEste é o texto original: ' + left_to_space_name + ', Este é o texto com a correção: ' + left_to_space_name.lstrip() + "!")
print('\t\tEste é o texto original: ' + space_both_sides_name + ', Este é o texto com a correção: ' + space_both_sides_name.strip() + "!")