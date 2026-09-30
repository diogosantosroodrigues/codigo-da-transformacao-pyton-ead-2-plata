def somar(a, b):
    """
    Soma dois números.
    """
    return a + b

def subtrair(a, b):
    """
    Subtrai o segundo número do primeiro.
    """
    return a - b

def potencia(base, expoente):
    """
    Calcula a potência de um número.
    """
    return base ** expoente

def multiplicar(a,b):

    return a * b

def dividir(a,b): 

    if b == 0:
        return "Erro: Divisão por Zero não Permitida"
    return a / b 

def divisao_inteira(a, b):
    """
    
    Retorna apenas a parte inteira da divisão de 'a' por 'b'.
    Parametros: a (int/float), b (int/float)
    Retorno: O resto da divisão ou uma mensagem de erro se b == 0.
    """
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a % b 