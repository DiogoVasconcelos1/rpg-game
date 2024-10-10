import random

# Classe base Personagem
class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def esta_vivo(self):
        return self.vida > 0

# Classe Heroi
class Heroi(Personagem):
    def __init__(self, nome, vida, ataque):
        # Chama o construtor da classe base Personagem
        super().__init__(nome, vida, ataque)
    
    def atacar(self, monstro):
        pass

# Subclasses de Heroi
class Guerreiro(Heroi):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)  # Passa atributos para Heroi (que passa para Personagem)
    
    def atacar(self, monstro):
        print(f"{self.nome} ataca com a espada!")
        monstro.receber_dano(self.ataque)

class Mago(Heroi):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)  # Passa atributos para Heroi (que passa para Personagem)
    
    def atacar(self, monstro):
        print(f"{self.nome} ataca com magia!")
        monstro.receber_dano(self.ataque)

# Classe Monstro
class Monstro(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)  # Passa atributos para Personagem
    
    def receber_dano(self, dano):
        pass

# Subclasses de Monstro
class Ogro(Monstro):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)  # Passa atributos para Monstro (que passa para Personagem)
    
    def receber_dano(self, dano):
        print(f"Ogro resiste ao ataque!")
        self.vida -= (dano // 2)  # Ogro recebe metade do dano

class Dragao(Monstro):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)  # Passa atributos para Monstro (que passa para Personagem)
    
    def receber_dano(self, dano):
        print(f"Dragão é fraco contra o ataque!")
        self.vida -= dano  # Dragão recebe o dano total
