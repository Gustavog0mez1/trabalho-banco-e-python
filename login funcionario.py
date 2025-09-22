import random

print("=== LOGIN FUNCIONÁRIO ===")
email = input("Email: ")
cpf = input("CPF: ")
if not cpf.isdigit():
    print("ERRO: CPF deve conter apenas números!")
else:
    senha = input("Senha: ")
    id_funcionario = random.randint(1, 1000)
    print(f"Login realizado! ID:{id_funcionario} Email:{email} CPF:{cpf}")
