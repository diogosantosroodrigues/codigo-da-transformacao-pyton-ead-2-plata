import sqlite3

conn = sqlite3.connect('atividade_info_cliente.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

clientes_iniciais = [
    ('Matheus Hideo', 'matheus@mail.com'),
    ('Antônio Alves', 'antonio@mail.com'),
    ('Alexandra Augusta', 'alexandra@mail.com'),
    ('Lucas Freitas', 'lucas@mail.com'),
    ('Arthur Augusto', 'arthur@mail.com'),
    ('Ana Alves', 'ana@mail.com')
]

cursor.executemany('''
    INSERT INTO clientes (nome, email) VALUES (?, ?)
''', clientes_iniciais)
conn.commit()


cursor.execute('''
    UPDATE clientes SET email = 'matheus.hideo@email.com' WHERE nome = 'Matheus Hideo'
''')
conn.commit()


cursor.execute('''
    DELETE FROM clientes WHERE nome = 'Lucas Freitas'
''')
conn.commit()


print("--- Lista de Clientes (CRUD) ---")
cursor.execute('SELECT * FROM clientes')
for cliente in cursor.fetchall():
    print(cliente)


print("\n--- Clientes que começam com 'A' ---")
cursor.execute("SELECT * FROM clientes WHERE nome LIKE 'A%'")
clientes_com_a = cursor.fetchall()

for cliente in clientes_com_a:
    print(cliente)


cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        status TEXT DEFAULT 'Pendente'
    )
''')


cursor.execute("INSERT INTO tarefas (descricao) VALUES ('Enviar atividade do Módulo 11')")
cursor.execute("INSERT INTO tarefas (descricao) VALUES ('Estudar Python e SQLite')")
conn.commit()


cursor.execute("DELETE FROM tarefas WHERE id = 2")
conn.commit()


print("\n--- Lista de Tarefas (Desafio Extra) ---")
cursor.execute("SELECT * FROM tarefas")
for tarefa in cursor.fetchall():
    print(tarefa)


conn.close()