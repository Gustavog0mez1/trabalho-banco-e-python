import random

print("=== CADASTRO CLIENTE ===")
email = input("Email: ")
nome = input("Nome: ")
cpf = input("CPF: ")
if not cpf.isdigit():
    print("ERRO: CPF deve conter apenas números!")
else:
    telefone = input("Telefone: ")
    idade = input("Idade: ")
    id_cliente = random.randint(1, 1000)
    print(f"Dados do cliente: ID:{id_cliente} Nome:{nome} Email:{email} CPF:{cpf} Telefone:{telefone} Idade:{idade}")
