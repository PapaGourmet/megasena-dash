import random

def genAleatorycolors(numero_cores):
    cores = []
    for _ in range(numero_cores):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        cor_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)

        cores.append(cor_hex)
    
    return cores


def categorizar(valor):
    if valor <= 2:
        return "forte"
    elif valor >= 3 and valor <= 4:
        return "intermediário"
    else:
        return "fraco"
    
def getExplanatoryText():
    text = 'Esse dados demostram que do ponto de vista estatístico, é possível definir a vulnerabilidade de uma combinação de jogos. É objetivo dessa demostração, determinar, por meio de análises gráficas, quais são os níveis de vulnerabilidade (desordem) de um combinação simples para jogos de 6 dezenas da mega sena'
    return '{}'.format(text)