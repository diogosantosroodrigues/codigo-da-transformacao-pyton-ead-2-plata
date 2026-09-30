# A classe carro e um exemplo para criar objetos de veiculos
# O __init__ inicia os 'marca' e 'modelo'
# O 'exibir info' retorna os dados formatados em texto

class Carro:
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo


        def exibir_info(self):
            return f"Marca: {self.marca}, Modelo: {self.modelo}"

        meu_carro = Carro("Ferari", "Fiesta")
        print(meu_carro.exibir_info())