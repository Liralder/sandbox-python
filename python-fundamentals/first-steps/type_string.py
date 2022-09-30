# Strings #
#
# Utilizando métodos para formatação de uma string  #
# O método title() exibe cada palavra com a letra inicial sendo maiúsculas   #
# O método upper() exibe cada palavra com todas as letras sendo maiúsculas   #
# o método lower() exibe cada palabra com todas as letras sendo minúsculas   #
name = 'gandalf, o cinzento'
#
print(name.title())
print(name.upper())
print(name.lower())
#
#
# Utilizando o (+) para combinar (concatenar) diferentes strings #
# Podemos utilizar a concatenação para criar mensagens simples e elegantes #
first_name = 'gandalf'
last_name = 'o cinzento'
full_name = first_name + ", " + last_name
#
message = "Hello, " + full_name.title() + "!"
#
print(message)
#
# Podemos utilizar também tabulações e quebras de linhas #
# \t: Tabulação #
# \n: Quebra de linha   #
print("\nMercado: \n\tArroz\n\tFeijão\n\tNescau")
#
# Podemos também remover espaços em branco que não queremos #
# .rstrip(): Remove espaços em branco a direita #
# .lstrip(): Remove espaços em branco a esquerda    #
# .strip(): Remove espaços em branco de ambos os lados  #
#
right_to_space = 'Este texto possuia um espaço em branco a direta '
left_to_space = ' Este texto possuia um espaço em branco a esquerda'
space_both_sides = ' Este texto possui espaço em branco de ambos os lados '
#
print('\nEste é o texto original: ' + right_to_space + ', Este é o texto com a correção: ' + right_to_space.rstrip() + "!")
print('Este é o texto original: ' + left_to_space + ', Este é o texto com a correção: ' + left_to_space.lstrip() + "!")
print('Este é o texto original: ' + space_both_sides + ', Este é o texto com a correção: ' + space_both_sides.strip() + "!")
#
# Um Ponto muito importante de entendermos é relacionado a aspas simples e duplas #
# Caso exista dentro do texto um apóstrofo o ideal é que se utilize a ("") #
#
print('\nNesse caso, o ideal é se utilizar as aspas duplas: ' + "One of Python's strengths is its diverse community.")
#
#