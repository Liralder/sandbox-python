# Hora de exercitar os conceitos.   #
print('\nExercitando o conhecimento:')
#
exemplo_first_name = 'Jack'
exemplo_last_name = 'Sparrow'
exemplo_message = 'Não quis esperar, mas o ' + exemplo_first_name + ' ' +  exemplo_last_name
print('\tArmazenando um nome de uma pessoa e exibindo uma mensagem pessoal: ' + exemplo_message + '.')
#
#
print('\tArmazenando um nome de uma pessoa e exibindo em minúsculo, maiúsculo, e apenas com as primeiras letras:')
print('\t\tMinúsculo: ' + exemplo_first_name.lower())
print('\t\tMaiúsculo: ' + exemplo_first_name.upper())
print('\t\tPrimeiras letras maiúsculas: ' + exemplo_first_name.title())
#
#
print('\tExibindo uma citação famosa e alternando as aspas: ' + 'Abraham Lincoln certa vez disse: "No final das contas, não são os anos de sua vida que contam. É a vida em seus anos."')
#
#
famous_person = 'Abraham Lincoln'
famous_citation = '"No final das contas, não são os anos de sua vida que contam. É a vida em seus anos."'
famous_message = famous_person + ' certa vez disse: ' + famous_citation
print('\tArmazenando uma citação famosa e alternando as aspas: ' + famous_message)
#
#
right_to_space_name = 'Gandalf, O Cinzento '
left_to_space_name = ' Gandalf, O Cinzento'
space_both_sides_name = ' Gandalf, O Cinzento ' 
print('\tArmaze o nome em uma variável com espaços em branco ao lado direito, esquerdo e em ambos, e exiba o dado original, e após a remoção do espaço em branco:')
print('\t\tEste é o texto original: ' + right_to_space_name + ', Este é o texto com a correção: ' + right_to_space_name.rstrip() + "!")
print('\t\tEste é o texto original: ' + left_to_space_name + ', Este é o texto com a correção: ' + left_to_space_name.lstrip() + "!")
print('\t\tEste é o texto original: ' + space_both_sides_name + ', Este é o texto com a correção: ' + space_both_sides_name.strip() + "!")
#
#