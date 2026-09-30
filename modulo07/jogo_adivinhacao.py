

import random
import math



print("Bem-vindo ao Jogo da Adivinhação!")
print("Eu escolhi um número entre 1 e 100.")
print("Tente adivinhá-lo!")


numero_secreto = random.randint(1, 100)
tentativas = 0


while True:
    try:
        
        palpite = int(input("\nDigite seu palpite: "))
        tentativas += 1

        diferenca = math.fabs(palpite - numero_secreto)

        
        if palpite == numero_secreto:
            print(f"\nParabéns! Você acertou o número em {tentativas} tentativas!")
            break 

        
        elif palpite < numero_secreto:
            print(f"Muito baixo! A diferença para o número secreto é de aproximadamente {int(diferenca)}.")
        else:
            print(f"Muito alto! A diferença para o número secreto é de aproximadamente {int(diferenca)}.")

    except ValueError:
        
        print("Entrada inválida. Por favor, digite um número inteiro.")