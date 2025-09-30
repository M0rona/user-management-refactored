usuarios = []
next_id = 1

def _get_next_id():
    """Função interna para incrementar e retornar o próximo ID."""
    global next_id
    current_id = next_id
    next_id += 1
    return current_id

def adicionar_usuario(nome: str, email: str) -> dict:
    """
    Adiciona um novo usuário à lista e retorna o objeto criado.
    Não tem dependências externas (I/O, email, API).
    """
    usuario = {
        "id": _get_next_id(),
        "nome": nome,
        "email": email,
        "ativo": True
    }
    usuarios.append(usuario)
    return usuario

def listar_usuarios() -> list:
    """Retorna uma cópia da lista de usuários para evitar mutação externa."""
    return list(usuarios)

def desativar_usuario(user_id: int) -> dict | None:
    """Desativa um usuário pelo ID e retorna o objeto, ou None se não encontrado."""
    for u in usuarios:
        if u["id"] == user_id:
            u["ativo"] = False
            return u
    return None

# Funções auxiliares para testes (opcional)
def _reset_usuarios():
    global usuarios, next_id
    usuarios = []
    next_id = 1