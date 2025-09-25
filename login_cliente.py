import random

print("=== LOGIN CLIENTE ===")
email = input("Email: ")
cpf = input("CPF: ")
if not cpf.isdigit() or len(cpf) != 11:
    print("ERRO: CPF deve conter apenas números e ter 11 dígitos!")
else:
    senha = input("Senha: ")
    id_cliente = random.randint(1000000000, 9999999999)
    print(f"Login realizado! ID:{id_cliente} Email:{email} CPF:{cpf}")
