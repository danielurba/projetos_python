"""
This program generates passages that are generated in mad-lib format
Author: Katherin 
"""

# The template for the story

STORY = """Esta manhã eu %s acordei me sentindo %s. Vai ser um dia %s! Do lado de fora, um monte de %ss protestavam para manter %s nas lojas. Eles começaram a comer
%ss ao ritmo do %s, o que fez com que todo o monte de %ss ficasem com muito %s. Preocupado, %s mandou uma mensagem para o(a) %s, que voou para %s e caiu na(o) %s, e
depois em uma poça de aguá %s. %s acordou no ano %s, em um mundo em que (a)os %ss governavam o mundo. """
print ("Biblioteca Bugada Começou !!!")
name = input ("Digite seu Nome:")
sentimento = input ("Sentimento Agora ?")
expressao = input ("Algum Elogio:")
animal = input ("Um Animal:")
comida = input ("Uma Comida:")
fruta = input ("Uma Fruta:")
musica = input ("Estilo Musical Favorito ?")
sentimento2 = input ("Outro Sentimento ?")
name2 = input ("Um outro Nome:")
pais = input ("Um País:")
sobremesa = input ("Sobremesa ?")
cor = input ("Uma cor:")
ano = input ("Um Ano ?")
animal2 = input ("Outro Animal:")
print (STORY % (name, sentimento, expressao, animal, comida, fruta, musica, animal, sentimento2, name, name2, pais, sobremesa, cor, name, ano, animal2))




