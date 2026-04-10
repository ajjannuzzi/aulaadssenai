class Pessoa:
    def __init__(self, nome, idade): #construtora
        self.nome = nome
        self.idade = idade #self serve para armazenar os valores dentro das classes
    def apresentar(self):
        print("Olá", self.nome)
        print("Você tem:", self.idade, "anos.")

pessoa1 = Pessoa("João", 30)
pessoa1.apresentar()

