from flask import Flask, jsonify
import pytest

# 1. Instância do serviço Flask
aplicacao = Flask(__name__)


@aplicacao.route("/api/calcular/<int:valor_a>/<int:valor_b>", methods=["GET"])
def rota_calculo_adicao(valor_a, valor_b):
    
    total = valor_a + valor_b
    return jsonify({"soma": total}), 200



@pytest.fixture
def cliente_teste():
    aplicacao.config["TESTING"] = True
    with aplicacao.test_client() as simulador:
        yield simulador


def test_endpoint_calculo_sucesso(cliente_teste):
    
    retorno = cliente_teste.get("/api/calcular/12/8")

    assert retorno.status_code == 200

    assert retorno.get_json() == {"soma": 20}