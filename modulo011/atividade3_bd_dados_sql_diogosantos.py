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

dados = [
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
cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?)', dados)
conn.commit()


print("=== CLIENTES QUE COMECAM COM 'A' ===")
cursor.execute("SELECT * FROM clientes WHERE nome LIKE 'A%'")
for linha in cursor.fetchall():
    print(f"ID: {linha[0]} | Nome: {linha[1]} | Email: {linha[2]}")

print("\n=== CLIENTES COM 'AUGUSTO/AUGUSTA' NO NOME ===")
cursor.execute("SELECT * FROM clientes WHERE nome LIKE '%August%'")
for linha in cursor.fetchall():
    print(f"ID: {linha[0]} | Nome: {linha[1]} | Email: {linha[2]}")

conn.close()