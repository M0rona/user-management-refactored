import user_management
import services.email_service as email_service
import services.external_api_service as api_service

def handle_adicionar_usuario():
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email: ")

    # 1. Lógica de Negócio (UserManagement)
    novo_usuario = user_management.adicionar_usuario(nome, email)
    
    # 2. Serviço Externo (EmailService)
    email_service.enviar_email_boas_vindas(novo_usuario)
    
    print(f"Usuário {nome} adicionado com sucesso!")
    handle_listar_usuarios()

def handle_listar_usuarios():
    usuarios = user_management.listar_usuarios()
    print("\nLista de Usuários:")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for u in usuarios:
            status = 'Ativo' if u['ativo'] else 'Inativo'
            print(f"{u['id']}: {u['nome']} ({u['email']}) - {status}")
    print()

def handle_desativar_usuario():
    try:
        user_id = int(input("Digite o ID do usuário para desativar: "))
    except ValueError:
        print("ID inválido!")
        return

    usuario_desativado = user_management.desativar_usuario(user_id)
    
    if usuario_desativado:
        print(f"Usuário {usuario_desativado['nome']} desativado.")
    else:
        print("Usuário não encontrado.")

def handle_buscar_usuario_api():
    try:
        user_id = int(input("Digite o ID do usuário para buscar na API: "))
    except ValueError:
        print("ID inválido!")
        return

    # 1. Serviço Externo (ExternalApiService)
    dados = api_service.buscar_usuario_api(user_id)
    
    if dados:
        print(f"Usuário encontrado na API: {dados['nome']} ({dados['email']})")
    else:
        print("Usuário não encontrado na API ou erro de conexão.")

def menu():
    while True:
        print("\n=== Sistema de Usuários (Refatorado) ===")
        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("3 - Desativar usuário")
        print("4 - Buscar usuário na API (Requests)")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            handle_adicionar_usuario()
        elif opcao == "2":
            handle_listar_usuarios()
        elif opcao == "3":
            handle_desativar_usuario()
        elif opcao == "4":
            handle_buscar_usuario_api()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()