import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('atividade_info_cliente.db')
cursor = conn.cursor()

# 1. Criar a tabela de Tarefas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        status TEXT DEFAULT 'Pendente'
    )
''')

# Limpa os dados anteriores para execução limpa no VS Code
cursor.execute('DELETE FROM tarefas')

# 2. Adicionar Tarefas (CREATE)
cursor.execute("INSERT INTO tarefas (descricao) VALUES ('Criar repositorio no GitHub')")
cursor.execute("INSERT INTO tarefas (descricao) VALUES ('Criar pasta Modulo_11')")
cursor.execute("INSERT INTO tarefas (descricao) VALUES ('Enviar exercicio resolvido')")
conn.commit()
print("Tarefas adicionadas com sucesso!\n")

cursor.execute("DELETE FROM tarefas WHERE id = 2")
conn.commit()
print("Tarefa com ID 2 removida com sucesso!\n")

print("=== SISTEMA DE GERENCIAMENTO DE TAREFAS ===")
cursor.execute("SELECT * FROM tarefas")
tarefas = cursor.fetchall()

for t in tarefas:
    print(f"ID: {t[0]} | Descrição: {t[1]} | Status: {t[2]}")

conn.close()