import unittest


def calcular_soma(numero1, numero2):
    return numero1 + numero2


class TestesOperacaoSoma(unittest.TestCase):

    def test_adicao_valores_positivos(self):
        retorno = calcular_soma(10, 15)
        self.assertEqual(retorno, 25)

    def test_adicao_valores_negativos(self):
        retorno = calcular_soma(-5, -8)
        self.assertEqual(retorno, -13)


if __name__ == "__main__":
    unittest.main()