import requests

def obter_previsao_tempo():
    
    municipio = input("Informe a cidade desejada: ").strip()
    
    if not municipio:
        print("Erro: É necessário digitar o nome de uma cidade.")
        return

    chave_acesso = "2d6690b51aa4015324c330bb1bfa1a7f"
    
    url_geocoding = f"http://api.openweathermap.org/geo/1.0/direct?q={municipio}&limit=1&appid={chave_acesso}"
    url_previsao = f"https://api.openweathermap.org/data/2.5/weather?q={municipio}&appid={chave_acesso}&lang=pt_br&units=metric"

    try:
        print("\nConsultando informações no OpenWeatherMap...")

        resposta_geo = requests.get(url_geocoding, timeout=5)
        resposta_geo.raise_for_status()
        
        dados_geo = resposta_geo.json()
        estado = dados_geo[0].get("state", "") if dados_geo else ""
        pais = dados_geo[0].get("country", "") if dados_geo else ""

        resposta_clima = requests.get(url_previsao, timeout=5)
        resposta_clima.raise_for_status()
        
        dados_clima = resposta_clima.json()

        nome_local = dados_clima.get("name", municipio)
        temp = dados_clima["main"]["temp"]
        sensacao = dados_clima["main"]["feels_like"]
        descricao = dados_clima["weather"][0]["description"]
        umidade_ar = dados_clima["main"]["humidity"]

        localizacao = f"{nome_local} - {estado}, {pais}" if estado else f"{nome_local}, {pais}"

        print("\n" + "=" * 40)
        print(f"🌍 PREVISÃO DO TEMPO: {localizacao}")
        print("=" * 40)
        print(f"🌤️  Condição   : {descricao.capitalize()}")
        print(f"🌡️  Temperatura: {temp:.1f}°C")
        print(f"🔥 Sensação   : {sensacao:.1f}°C")
        print(f"💧 Umidade    : {umidade_ar}%")
        print("=" * 40)

    except requests.exceptions.HTTPError as erro_http:
        status = erro_http.response.status_code
        if status == 401:
            print("\n❌ Erro 401: Chave de API não autorizada.")
        elif status == 404:
            print(f"\n❌ Erro 404: Cidade '{municipio}' não foi localizada.")
        else:
            print(f"\n❌ Erro HTTP {status}: Não foi possível processar a requisição.")

    except requests.exceptions.ConnectionError:
        print("\n❌ Erro de Conexão: Falha ao conectar à rede. Verifique sua internet.")

    except requests.exceptions.Timeout:
        print("\n❌ Tempo limite excedido: O servidor demorou para responder.")

    except requests.exceptions.RequestException as erro:
        print(f"\n⚠️ Falha na requisição: {erro}")

if __name__ == "__main__":
    obter_previsao_tempo()