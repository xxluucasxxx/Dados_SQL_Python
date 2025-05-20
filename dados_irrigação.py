#!/usr/bin/env python3
# script.py – Armazenamento de dados de sensores em SQLite com CRUD
# Lucas Samuel – FarmTech Solutions (Fase 3, Entrega 2)

import sqlite3
from datetime import datetime

DB_FILENAME = 'dados_irriga.db'

def conectar():
    """Cria conexão e tabela se não existir."""
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS dados_sensor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fosforo INTEGER,
            potassio INTEGER,
            ph REAL,
            umidade REAL,
            irrigacao_ativa INTEGER,
            data_hora TEXT
        );
    """)
    conn.commit()
    return conn

def criar_registro(conn, fosforo, potassio, ph, umidade, irrigacao_ativa):
    """Insere um novo registro na tabela."""
    cur = conn.cursor()
    agora = datetime.now().isoformat(sep=' ', timespec='seconds')
    cur.execute("""
        INSERT INTO dados_sensor
        (fosforo, potassio, ph, umidade, irrigacao_ativa, data_hora)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (fosforo, potassio, ph, umidade, irrigacao_ativa, agora))
    conn.commit()
    return cur.lastrowid

def ler_registros(conn, filtro=None):
    """Lê e retorna registros; se filtro for SQL (ex: "irrigacao_ativa=1"), aplica."""
    cur = conn.cursor()
    sql = "SELECT * FROM dados_sensor"
    if filtro:
        sql += " WHERE " + filtro
    cur.execute(sql)
    return cur.fetchall()

def atualizar_registro(conn, registro_id, **campos):
    """Atualiza campos de um registro pelo id."""
    cur = conn.cursor()
    keys = ', '.join(f"{k}=?" for k in campos.keys())
    vals = list(campos.values()) + [registro_id]
    cur.execute(f"UPDATE dados_sensor SET {keys} WHERE id=?", vals)
    conn.commit()
    return cur.rowcount

def deletar_registro(conn, registro_id):
    """Remove um registro pelo id."""
    cur = conn.cursor()
    cur.execute("DELETE FROM dados_sensor WHERE id=?", (registro_id,))
    conn.commit()
    return cur.rowcount

def exemplo_de_uso():
    conn = conectar()
    # 1) Criar registros de exemplo
    criar_registro(conn, fosforo=1, potassio=1, ph=6.8, umidade=35.2, irrigacao_ativa=1)
    criar_registro(conn, fosforo=0, potassio=1, ph=7.2, umidade=50.0, irrigacao_ativa=0)

    # 2) Ler todos
    print("TODOS OS REGISTROS:")
    for row in ler_registros(conn):
        print(row)

    # 3) Atualizar um registro
    atualizar_registro(conn, registro_id=1, ph=6.5, umidade=34.0)
    print("\nAPÓS ATUALIZAÇÃO DO ID=1:")
    print(ler_registros(conn, filtro="id=1"))

    # 4) Deletar o segundo registro
    deletar_registro(conn, registro_id=2)
    print("\nAPÓS EXCLUSÃO DO ID=2:")
    print(ler_registros(conn))

    conn.close()

if __name__ == '__main__':
    exemplo_de_uso()
