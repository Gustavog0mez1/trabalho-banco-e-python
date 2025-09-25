import random
import hashlib
import string

print("=== CADASTRO CLIENTE ===")
email = input("Email: ")
nome = input("Nome: ")
cpf = input("CPF: ")
if not cpf.isdigit() or len(cpf) != 11:
    print("ERRO: CPF deve conter apenas números e ter 11 dígitos!")
else:
    telefone = input("Telefone: ")
    if not telefone.isdigit():
        print("ERRO: Telefone deve conter apenas números!")
    else:
        idade = input("Idade: ")
        if not idade.isdigit() or len(idade) > 3:
            print("ERRO: Idade deve conter apenas números e no máximo 3 dígitos!")
        else:
            # Gera senha com letras, números e caracteres especiais
            caracteres = string.ascii_letters + string.digits + "!@#$%&*"
            senha_aleatoria = ''.join(random.choice(caracteres) for _ in range(8))
            id_cliente = random.randint(1000000000, 9999999999)
            senha_criptografada = hashlib.md5(senha_aleatoria.encode()).hexdigest()
            print(f"Cliente cadastrado! ID:{id_cliente} Nome:{nome} Email:{email} CPF:{cpf} Telefone:{telefone} Idade:{idade} Senha Aleatória:{senha_aleatoria} Senha Criptografada:{senha_criptografada}")
