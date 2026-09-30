from faker import Faker

faker = Faker('pt_BR')  

print("Gerando 5 perfis de usuários com dados falsos:\n")

for i in range(5):
    nome = faker.name()
    endereco = faker.address()
    email = faker.email()
    
    print(f"--- Perfil {i+1} ---")
    print(f"Nome: {nome}")
    print(f"Endereço: {endereco}")
    print(f"Email: {email}")
    print("-" * 20)