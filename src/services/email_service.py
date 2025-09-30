from datetime import datetime
import os

LOG_FILE = "log_email.txt" # O caminho será resolvido a partir de onde o script principal é executado

def salvar_log_email(usuario: dict, mensagem: str):
    """Salva o log do email enviado em um arquivo."""
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now()} - {usuario['email']} - {mensagem}\n")
    except Exception as e:
        print(f"Erro ao salvar o log de email: {e}")

def enviar_email_boas_vindas(usuario: dict):
    """Simula o envio de um email de boas-vindas e chama o log."""
    mensagem = f"Olá {usuario['nome']}, bem-vindo ao sistema!"
    print(f"[EMAIL SIMULADO] Enviando para {usuario['email']}: {mensagem}")
    salvar_log_email(usuario, mensagem)