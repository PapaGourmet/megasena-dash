lista_de_nomes = ['a', 'b', 'c']

# Crie um dicionário vazio para armazenar as listas
listas_dinamicas = {}

# Itere sobre a lista de nomes e crie dinamicamente as listas
for nome in lista_de_nomes:
    listas_dinamicas[nome] = []

# Exemplo de como adicionar elementos às listas dinâmicas
listas_dinamicas['a'].append(1)
listas_dinamicas['b'].append(2)
listas_dinamicas['c'].append(3)

# Imprima as listas dinâmicas
print(listas_dinamicas)
