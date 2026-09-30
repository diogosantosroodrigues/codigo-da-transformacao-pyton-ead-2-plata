import requests

def consultar_cotacao_moedas():
    
    endpoint_economia = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"

    
    try:
        print("Enviando requisição ao serviço de câmbio...")
        
        
        resposta = requests.get(endpoint_economia, timeout=5)
        resposta.raise_for_status()

        
        informacoes_cambio = resposta.json()
        print("Conexão estabelecida e dados recebidos com sucesso!\n")

        
        dados_dolar = informacoes_cambio.get("USDBRL", {})
        
        nome_moeda = dados_dolar.get("name", "Dólar Americano/Real Brasileiro")
        valor_compra = float(dados_dolar.get("bid", 0.0))

        
        print("=" * 40)
        print(f"Moeda  : {nome_moeda}")
        print(f"Compra : R$ {valor_compra:.2f}")
        print("=" * 40)

    except requests.exceptions.HTTPError as erro_http:
        print(f"❌ Erro na resposta do servidor HTTP: {erro_http}")

    except requests.exceptions.ConnectionError:
        print("❌ Erro de Conexão: Não foi possível conectar ao serviço. Verifique sua rede.")

    except requests.exceptions.Timeout:
        print("❌ Tempo Esgotado: O servidor demorou muito para responder.")

    except requests.exceptions.RequestException as erro_geral:
        print(f"⚠️ Erro inesperado ao consultar a API: {erro_geral}")


if __name__ == "__main__":
    consultar_cotacao_moedas()