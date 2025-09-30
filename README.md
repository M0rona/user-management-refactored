# Gerenciamento de Usuários - Refatorado em Python

Este projeto é uma **refatoração** do código original em Python, focada em melhorar a **organização**, **reduzir o acoplamento** e aumentar a **testabilidade** do sistema através do princípio da **Separação de Responsabilidades (SRP)**.

## Participantes
* Gabriel Morona Coelho
* Lucas Sernajoto Vanzeler Paixão

---

## 🚀 Estrutura e Princípios de Design

O código foi dividido em módulos específicos, isolando as responsabilidades:

| Módulo | Responsabilidade Principal | Dependências Isoladas |
| :--- | :--- | :--- |
| **`src/user_management.py`** | **Lógica de Negócio**. Gerencia o estado dos usuários (adicionar, listar, desativar). | Nenhuma dependência externa (I/O, rede, arquivo). **Altamente testável.** |
| **`src/services/email_service.py`** | **Serviço de Email/Log**. Simula o envio de email e manipula o arquivo `log_email.txt`. | `datetime`, `os` (manipulação de arquivo). |
| **`src/services/external_api_service.py`** | **Serviço de API Externa**. Lida com requisições HTTP para buscar usuários na API externa. | Biblioteca `requests`. |
| **`src/cli.py`** | **Interface de Usuário (Orquestrador)**. Lida com `input()` e `print()` e orquestra as chamadas entre a lógica de negócio e os serviços. | Depende de todos os outros módulos. |

## 📦 Gerenciamento de Dependências

A biblioteca externa **`requests`** foi escolhida para lidar com as requisições HTTP na função de busca na API.

O gerenciamento de pacotes é feito pelo **`pip`**, utilizando o arquivo `requirements.txt`.

### Conteúdo de `requirements.txt`

requests>=2.31.0


---

## ⚙️ Instruções de Execução

Siga os passos abaixo para configurar e executar o projeto.

### 1. Pré-requisitos

* **Python 3.8+** instalado.

### 2. Configuração do Ambiente Virtual

É altamente recomendado o uso de um ambiente virtual (`venv`) para isolar as dependências do projeto:

```bash
# 1. Crie o ambiente virtual na pasta raiz do projeto
python -m venv venv

# 2. Ative o ambiente virtual
# No Linux/macOS:
source venv/bin/activate

# No Windows (PowerShell):
# .\venv\Scripts\Activate.ps1
```

### 3. Instalação das Dependências

Com o ambiente virtual ativo, instale a biblioteca requests usando o arquivo de requisitos:
```bash
pip install -r requirements.txt
```

### 4. Execução do Sistema

Execute o script principal (cli.py) a partir da raiz do projeto:
Bash

```bash
python src/cli.py
```

### 5. Finalização

Para desativar o ambiente virtual após o uso:
Bash

```bash
deactivate
```
