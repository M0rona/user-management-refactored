import requests

API_BASE_URL = "https://jsonplaceholder.typicode.com/users"

def buscar_usuario_api(user_id: int) -> dict | None:
    """
    Busca um usuário pelo ID na API externa.
    Retorna um dicionário com nome e email, ou None se não encontrado.
    """
    try:
        r = requests.get(f"{API_BASE_URL}/{user_id}")
        r.raise_for_status() # Lança exceção para status codes 4xx/5xx
        
        dados = r.json()
        return {
            "nome": dados.get("name"),
            "email": dados.get("email")
        }
    except requests.exceptions.HTTPError as e:
        if r.status_code == 404:
            return None  # Usuário não encontrado
        raise # Lança outros erros HTTP
    except requests.exceptions.RequestException as e:
        # Lidar com erros de conexão, timeout, etc.
        print(f"[ERRO DE CONEXÃO] Falha ao conectar com a API: {e}")
        return None