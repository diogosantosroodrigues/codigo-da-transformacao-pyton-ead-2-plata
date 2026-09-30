# CLASSE: carro 
# CLASSE Carro: Cria e gerencia dados de veículos gerais
# CLASSE CarroEletrico: Herda de Carro e adiciona bateria
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo}"


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        info_base = super().exibir_info()
        return f"{info_base} | Autonomia: {self.autonomia_bateria} km"


meu_ev = CarroEletrico("Tesla", "Model Y", 450)
print(meu_ev.exibir_info())