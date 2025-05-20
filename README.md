# Entrega 2 – Armazenamento de Dados em SQL com Python

**Autor:** Lucas Samuel  
**Projeto:** FarmTech Solutions – Fase 3 – Entrega 2

---

## 1. Visão Geral
Este script em Python conecta-se a um banco de dados SQLite (`dados_irriga.db`), cria a tabela `dados_sensor` (caso não exista) e oferece funções para **CRUD** (Create, Read, Update, Delete) dos dados coletados pelo ESP32.

---

## 2. Estrutura da Tabela (MER Fase 2)
A tabela reflete o **Modelo Entidade-Relacionamento** da Fase 2:

- **dados_sensor** (Entidade)  
  - **id** (PK)  
  - **fosforo**, **potassio**, **ph**, **umidade**, **irrigacao_ativa** (Atributos)  
  - **data_hora** (Timestamp da leitura)

---

## 3. Como Executar

1. **Pré-requisitos**:  
   - Python 3.x instalado  
   - Biblioteca padrão `sqlite3` (já incluída no Python)

2. **Rodar o script**:  
   ```bash
   python3 script.py

O script irá:

    Criar o banco e a tabela (se necessário)

    Inserir registros de exemplo

    Exibir operações de Read, Update e Delete no terminal

4. Funções CRUD

    criar_registro(...) – Insere nova leitura

    ler_registros(...) – Retorna todas ou filtradas

    atualizar_registro(...) – Modifica campos de um ID

    deletar_registro(...) – Remove um registro por ID

5. Estrutura da Pasta

Entrega2_SQL_Python/
├── dados_irrigação.py
.py
└── README.md
