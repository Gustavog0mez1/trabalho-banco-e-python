import random

print("=== CADASTRO FUNCIONARIO ===")
email = input("Email: ")
nome = input("Nome: ")
cpf = input("CPF: ")
if not cpf.isdigit():
    print("ERRO: CPF deve conter apenas números!")
else:
    telefone = input("Telefone: ")
    idade = input("Idade: ")
    id_funcionario = random.randint(1, 1000)
    print(f"Dados do funcionario: ID:{id_funcionario} Nome:{nome} Email:{email} CPF:{cpf} Telefone:{telefone} Idade:{idade}")
