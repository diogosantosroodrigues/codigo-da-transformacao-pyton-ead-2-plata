import unittest



class OperacoesMatematicas:

    def adicao(self, x, y):
        return x + y

    def divisao(self, x, y):
        if y == 0:
            
            raise ValueError("Divisão por zero não é permitida.")
        return x / y



class TestesOperacoesMatematicas(unittest.TestCase):

    
    def setUp(self):
        self.operador = OperacoesMatematicas()

    def test_operacao_adicao(self):
    
        self.assertEqual(self.operador.adicao(20, 8), 28)

    def test_operacao_divisao_valida(self):
       
        self.assertEqual(self.operador.divisao(50, 5), 10)

    def test_operacao_divisao_com_zero(self):
        
        with self.assertRaises(ValueError):
            self.operador.divisao(15, 0)


if __name__ == "__main__":
    unittest.main()