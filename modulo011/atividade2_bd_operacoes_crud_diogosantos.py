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

cursor.execute('DELETE FROM clientes')

dados_iniciais = [
    ('Matheus Hideo', 'matheus@mail.com'), 
    ('Antônio Alves', 'antonio@mail.com'),
    ('Alexandra Augusta', 'alexandra@mail.com'), 
    ('Lucas Freitas', 'lucas@mail.com'),
    ('Arthur Augusto', 'arthur@mail.com'), 
    ('Ana Alves', 'ana@mail.com'),
    ('Jhonatas Nascimento', 'jhonatas@mail.com'), 
    ('Antônio Alberto', 'alberto@mail.com'),
    ('Alex Augustinho', 'alex@mail.com'), 
    ('Adriana Almeida', 'adriana@mail.com'),
    ('Angélica Andrade', 'angelica@mail.com'), 
    ('Alê Alvarenga', 'ale@mail.com')
]
cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?)', dados_iniciais)
conn.commit()

cursor.execute('UPDATE clientes SET email = ? WHERE nome = ?', ('hideo.novo@mail.com', 'Matheus Hideo'))
conn.commit()

cursor.execute('DELETE FROM clientes WHERE nome = ?', ('Lucas Freitas',))
conn.commit()


print("=== TODOS OS CLIENTES CADASTRADOS ===")
cursor.execute('SELECT * FROM clientes')
for cliente in cursor.fetchall():
    print(cliente)


print("\n=== CLIENTES QUE COMECAM COM A LETRA 'A' ===")
cursor.execute("SELECT * FROM clientes WHERE nome LIKE 'A%'")
for cliente in cursor.fetchall():
    print(cliente)


cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL
    )
''')

cursor.execute('DELETE FROM tarefas')

cursor.execute("INSERT INTO tarefas (descricao) VALUES ('Entregar atividade no GitHub')")
cursor.execute("INSERT INTO tarefas (descricao) VALUES ('Estudar Python no VS Code')")
conn.commit()

cursor.execute("DELETE FROM tarefas WHERE id = 1")
conn.commit()

print("\n=== LISTA DE TAREFAS (DESAFIO EXTRA) ===")
cursor.execute("SELECT * FROM tarefas")
for tarefa in cursor.fetchall():
    print(tarefa)

conn.close()