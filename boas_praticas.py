"""
python tem uma serie de convençoes e melhores praticas codificadas em PEPs (proposats de melhoria do python)
A mais conhecidas destas é provavelmente a PEP 8, que cobre o estilo de codificação

PEP 8 é o guia de estilo de codificaçao em python. ele inclui convençoes sobre nomes de variaveis, uso de espaços
em branco, comprimento da linha e muitas outras coisas que ajudam a manter o codigo python consistente e legível

Principais recomendaçoes da PEP 8:
algumas das principais recomendaçoes da PEP 8 incluem usar 4 espaços para a identaçao, limitar as linhas a 79 caracteres,
usar nomes de variaveis em snake_case para funçoes e variaveis e em CamelCase para classes
"""

def somar_valores(arguemnto_1, argumento_2):
    pass

class ContaBancaria():
    pass

"""
Uso de ferramentas de checagem de estilo
Para nos ajudar a seguir recomendaçoes da PEP 8, podemos usar ferramentas de checagem de estilo como flake8.
essas verramentas verificam nosso codigo e nos informam onde estamos desviando do guia estilo

pip install flack8
flack8 meu_script.py

Formataçao automatica de codigo
black é uma ferramenta de formataçao de codigo python que segue a filosofia "formato unico". Black formata todo o seu arquivo
em um estilo consistente, simplificando a tarefa de manter o codigo em conformidade com a PEP 8

pip install black
black meu_script.py

Organizaçao de imports com isort
isort é uma ferramenta python para classificar importaçoes alfabeticamente e separalas automaticamente em seçoes. ele proporciona
uma maneirta rapida e facil de ordenar e categorizar suas importaçoes

pip install isort
insort meu_script.py
"""