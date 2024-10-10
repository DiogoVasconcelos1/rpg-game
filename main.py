import random
from dados import escolher_heroi, gerar_monstro

def batalha(heroi, monstro):
    print(f"\nBatalha começa entre {heroi.nome} e {monstro.nome}!\n")

    while heroi.esta_vivo() & monstro.esta_vivo():
        input(f"{heroi.nome}, pressione Enter para continuar: ")
        # Turno do herói
        heroi.atacar(monstro)
        print(f"Vida do {monstro.nome}: {monstro.vida}")
        if not monstro.esta_vivo():
            print(f"{monstro.nome} foi derrotado!")
            break

        input(f"{monstro.nome} está prestes a atacar! Pressione Enter para continuar: ")
        # Turno do monstro
        print(f"{monstro.nome} ataca!")
        heroi.vida -= monstro.ataque
        print(f"Vida do {heroi.nome}: {heroi.vida}")
        if not heroi.esta_vivo():
            print(f"{heroi.nome} foi derrotado!")
            break

# Executa o jogo
if __name__ == "__main__":
    heroi = escolher_heroi()
    monstro = gerar_monstro()

    # Pergunta se o usuário está pronto para começar a batalha
    input("\nVocê está pronto para começar a batalha? Pressione Enter para começar: ")

    # Inicia a batalha
    batalha(heroi, monstro)
