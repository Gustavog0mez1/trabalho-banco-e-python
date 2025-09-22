import random

print("=== LOGIN CLIENTE ===")
email = input("Email: ")
cpf = input("CPF: ")
if not cpf.isdigit():
    print("ERRO: CPF deve conter apenas números!")
else:
    senha = input("Senha: ")
    id_cliente= random.randint(1, 1000)
    print(f"Login realizado! ID:{id_cliente} Email:{email} CPF:{cpf}")
