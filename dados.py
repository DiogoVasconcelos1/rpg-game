import random
from model import Guerreiro, Mago, Ogro, Dragao

# Função para criar herói com base na escolha do usuário
def escolher_heroi():
    while True:  # Continua pedindo até o usuário fazer uma escolha válida
        print("Escolha seu herói:")
        print("1. Guerreiro")
        print("2. Mago")
        
        try:
            escolha = int(input("Digite o número do herói desejado: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite 1 para Guerreiro ou 2 para Mago.")
            continue  # Se não for um número, volta ao início do loop

        if escolha == 1:
            return Guerreiro("Guerreiro", 100, 20)
        elif escolha == 2:
            return Mago("Mago", 80, 50)
        else:
            print("Opção inválida. Por favor, escolha 1 para Guerreiro ou 2 para Mago.")
            # O loop continua até que o usuário faça uma escolha válida


# Função para gerar monstro aleatório
def gerar_monstro():
    monstro_escolhido = random.choice([Ogro("Ogro", 120, 10), Dragao("Dragão", 150, 15)])
    return monstro_escolhido
