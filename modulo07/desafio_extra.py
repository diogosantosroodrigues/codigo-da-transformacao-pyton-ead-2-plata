

def criar_usuario(nome, email):
    """Cria e retorna um dicionário com os dados do usuário."""
    return {
        "nome": nome,
        "email": email,
        "status": "Ativo"
    }

def exibir_usuario(usuario):
    """Formata e exibe os dados do usuário."""
    print("--- Dados do Usuário ---")
    print(f"Nome: {usuario['nome']}")
    print(f"E-mail: {usuario['email']}")
    print(f"Status: {usuario['status']}\n")

def processar_pagamento(valor, forma_pagamento):
    """Simula o processamento de um pagamento."""
    return {
        "valor": valor,
        "forma_pagamento": forma_pagamento,
        "sucesso": True,
        "mensagem": f"Pagamento de R$ {valor:.2f} via {forma_pagamento} aprovado!"
    }



print("=== DESAFIO EXTRA: PACOTES E MÓDULOS ===")


novo_usuario = criar_usuario("Igor Freitas", "igor@email.com")
exibir_usuario(novo_usuario)


resultado = processar_pagamento(150.00, "Cartão de Crédito")

if resultado["sucesso"]:
    print(f"Status: {resultado['mensagem']}")
else:
    print("Erro ao processar pagamento.")