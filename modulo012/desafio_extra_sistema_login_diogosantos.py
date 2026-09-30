import pytest
from flask import Flask, jsonify, request


aplicacao = Flask(__name__)


CATALOGO_ITENS = [
    {"id": 101, "descricao": "Teclado RGB", "valor": 250.0},
    {"id": 102, "descricao": "Mouse Sem Fio", "valor": 120.0},
]


@aplicacao.route("/api/itens", methods=["GET"])
def buscar_todos_itens():
    """Retorna o catálogo completo de itens."""
    return jsonify(CATALOGO_ITENS), 200


@aplicacao.route("/api/itens/<int:item_id>", methods=["GET"])
def buscar_item_por_codigo(item_id):
    """Busca e retorna um item específico com base no ID."""
    item_localizado = next(
        (item for item in CATALOGO_ITENS if item["id"] == item_id), None
    )
    if item_localizado:
        return jsonify(item_localizado), 200
    return jsonify({"mensagem_erro": "Registro não localizado"}), 404


@aplicacao.route("/api/itens", methods=["POST"])
def cadastrar_novo_item():
    """Realiza o cadastro de um novo item com validação dos parâmetros de entrada."""
    conteudo = request.get_json()

  
    if (
        not conteudo
        or "descricao" not in conteudo
        or "valor" not in conteudo
    ):
        return (
            jsonify(
                {
                    "mensagem_erro": "Campos 'descricao' e 'valor' são obrigatórios."
                }
            ),
            400,
        )

    registro_criado = {
        "id": len(CATALOGO_ITENS) + 101,
        "descricao": conteudo["descricao"],
        "valor": float(conteudo["valor"]),
    }
    CATALOGO_ITENS.append(registro_criado)
    return jsonify(registro_criado), 201




@pytest.fixture
def cliente_amb_teste():
    """Instância simulada do cliente para disparo de requisições de teste."""
    aplicacao.config["TESTING"] = True
    with aplicacao.test_client() as simulador:
        yield simulador

    global CATALOGO_ITENS
    CATALOGO_ITENS = [
        {"id": 101, "descricao": "Teclado RGB", "valor": 250.0},
        {"id": 102, "descricao": "Mouse Sem Fio", "valor": 120.0},
    ]




def test_obter_catalogo_completo(cliente_amb_teste):
    """Valida o retorno geral do catálogo de itens e o status HTTP 200."""
    resposta = cliente_amb_teste.get("/api/itens")

    assert resposta.status_code == 200
    resultado = resposta.get_json()
    assert isinstance(resultado, list)
    assert len(resultado) == 2
    assert resultado[0]["descricao"] == "Teclado RGB"


def test_obter_item_especifico_com_sucesso(cliente_amb_teste):
    """Garante a busca correta de um registro cadastrado."""
    resposta = cliente_amb_teste.get("/api/itens/102")

    assert resposta.status_code == 200
    resultado = resposta.get_json()
    assert resultado["id"] == 102
    assert resultado["descricao"] == "Mouse Sem Fio"


def test_obter_item_nao_cadastrado(cliente_amb_teste):
    """Verifica se o sistema responde com 404 ao buscar por registro inexistente."""
    resposta = cliente_amb_teste.get("/api/itens/888")

    assert resposta.status_code == 404
    resultado = resposta.get_json()
    assert "mensagem_erro" in resultado
    assert resultado["mensagem_erro"] == "Registro não localizado"


def test_inserir_item_corretamente(cliente_amb_teste):
    """Testa a criação bem-sucedida de um novo elemento via POST."""
    novo_payload = {"descricao": "Monitor Ultrawide", "valor": 1800.0}

    resposta = cliente_amb_teste.post("/api/itens", json=novo_payload)

    assert resposta.status_code == 201
    resultado = resposta.get_json()
    assert resultado["id"] == 103
    assert resultado["descricao"] == "Monitor Ultrawide"


def test_falha_ao_inserir_item_sem_dados(cliente_amb_teste):
    """Confirma que requisições incompletas geram erro 400."""
    payload_incompleto = {"descricao": "Cadeira Ergonômica"}

    resposta = cliente_amb_teste.post("/api/itens", json=payload_incompleto)

    assert resposta.status_code == 400
    resultado = resposta.get_json()
    assert "mensagem_erro" in resultado
    assert "obrigatórios" in resultado["mensagem_erro"]