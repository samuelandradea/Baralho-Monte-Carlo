import random
from collections import Counter

def criar_baralho():
    baralho = []
    naipes = ['Copas', 'Espadas', 'Ouro', 'Paus']
    
    for naipe in naipes:
        baralho.append(('A' + naipe, 1))
        
        for valor in range(2, 11):
            baralho.append((str(valor) + naipe, valor))
        
        baralho.append(('J' + naipe, 10))
        baralho.append(('Q' + naipe, 10))
        baralho.append(('K' + naipe, 10))
    
    return baralho

def simular_uma_vez():
    baralho = criar_baralho()
    random.shuffle(baralho)
    tres_cartas = random.sample(baralho, 3)
    soma = sum(carta[1] for carta in tres_cartas)
    return soma

def simulacao_monte_carlo(num_simulacoes=100000):
    print("SAMUEL ANDRADE E CAIO CORDEIRO\n")
    print(f"Executando {num_simulacoes:,} simulações...\n")
    
    sucessos = 0
    distribuicao = Counter()
    
    for i in range(num_simulacoes):
        soma = simular_uma_vez()
        distribuicao[soma] += 1
        
        if soma == 21:
            sucessos += 1
        
        if (i + 1) % 10000 == 0:
            prob_parcial = (sucessos / (i + 1)) * 100
            print(f"Simulação {i + 1:,}: Probabilidade parcial = {prob_parcial:.4f}%")
    
    probabilidade = (sucessos / num_simulacoes) * 100
    
    print("\n")
    print(f"Total de simulações: {num_simulacoes:,}")
    print(f"Sucessos (soma = 21): {sucessos:,}")
    print(f"Probabilidade estimada: {probabilidade:.4f}%")
    print(f"Probabilidade em fração: {sucessos}/{num_simulacoes}")
    
    return probabilidade, sucessos, num_simulacoes

if __name__ == "__main__":
    simulacao_monte_carlo(100000)